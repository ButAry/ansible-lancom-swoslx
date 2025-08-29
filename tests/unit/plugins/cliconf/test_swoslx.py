import pytest
import json
import re

from unittest.mock import MagicMock, call
from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils._text import to_bytes, to_text

from ansible_collections.lancom.swoslx.plugins.cliconf.swoslx import Cliconf

# Extract test data into constants
SYSTEM_OUTPUT = b"""
Model Name                  : LANCOM GS-3510XP
System Description          : Managed L2+ PoE+ Switch, 4x 10/100/1000Base-T ports + 4x 100M/1G/2,5G ports + 2x 1G/10G SFP+ slots
Location                    : 
Contact                     : 
System Name                 : GS-3510XP
System Date                 : 2022-01-01T01:42:36+01:00
System Uptime               : 0d 00:43:51
Bootloader Version          : V1.05
Firmware Version            : 4.30.0147RU4
Hardware Version            : B1
Mechanical Version          : v1.01
Production Date             : 2024-05-06
Serial Number               : 4006396720100720
MAC Address                 : 00-a0-57-96-48-87
Total Memory                : 500MB
Free Memory                 : 335MB
Fan Speed                   : 0
Temperature 1               : 58
Temperature 2               : 43
Power                       : 1V0:1.04V; 2V5:2.53V; 12V:11.90V; 0V95:0.98V; 3V3:3.23V
"""

VERSION_OUTPUT = b"""

MAC Address      : 00-a0-57-96-48-87
Previous Restart : Cold

System Contact   : 
System Name      : GS-3510XP
System Location  : 
System Time      : 2022-01-01T01:43:14+01:00
System Uptime    : 00:44:29


Bootloader
----------
Image            : RedBoot 
Version          : version V1.05
Date             : 18:27:14, Jul 16 2020

Primary Image
-------------
Image            : linux (Active)
Version          : 4.30.0147RU4
Date             : 2025-01-20T09:46:05+01:00
Upload filename  : LC-GS-3510XP-4.30.0147-RU4.upx  

Backup Image
------------
Image            : linux.bk 
Version          : 4.30.0072RU1
Date             : 2024-07-18T15:29:44+02:00
Upload filename  : LC-GS-3510XP-4.30.0072-RU1.mfi

------------------
SID : 1 
------------------
Chipset ID       : VSC7440 Rev. B
Board Type       : SparX-IV_34
Flash Type       : NOR-only
Port Count       : 10
Product          : Microchip GS-3510XP Switch
Software Version : 4.30.0147RU4
Build Date       : 2025-01-20T09:46:05+01:00
Code Revision    : 98e6cfb3e
PoE Version      : HW Ver.:0, Prod:28, sw ver:224, param:19, build:2, internal sw ver:756, Asic Patch Num:20046

"""

class TestCliconf:
    @pytest.fixture
    def cliconf(self):
        plugin = Cliconf(connection=MagicMock())
        plugin._exec_cli_command = MagicMock()
        plugin._get_prompt = MagicMock()
        return plugin

    def test_get_device_info_successful(self, cliconf):
        system_lines = [line.strip() for line in SYSTEM_OUTPUT.splitlines()]
        version_lines = [line.strip() for line in VERSION_OUTPUT.splitlines()]

        # Monkey patch the get method to return different outputs for the two commands
        cliconf.get = MagicMock(side_effect=[
            system_lines,   # First call for 'show system'
            version_lines   # Second call for 'show version'
        ])

        # Call the function
        result = cliconf.get_device_info()

        # Assert all expected fields were parsed correctly
        assert "network_os" in result and result["network_os"] == "lancom.swoslx"
        assert "network_os_model" in result and result["network_os_model"] == "LANCOM GS-3510XP"
        assert "description" in result and result["description"].startswith("Managed L2+ PoE+ Switch, 4x 10/100/1000Base-T ports + 4x 100M/1G/2,5G ports + 2x 1G/10G SFP+ slots")
        assert "network_os_hostname" in result and result["network_os_hostname"] == "GS-3510XP"
        assert "serial_number" in result and result["serial_number"] == "4006396720100720"
        assert "macaddress" in result and result["macaddress"] == "00-a0-57-96-48-87"
        assert "manufactured_date" in result and result["manufactured_date"] == "2024-05-06"
        assert "network_os_image" in result and result["network_os_image"] == "LC-GS-3510XP-4.30.0147-RU4.upx"
        assert "network_os_version" in result and result["network_os_version"] == "4.30.0147RU4"

    def test_get_device_info_missing_data(self, cliconf):
        minimal_system_output = [
            line.strip() for line in b"""
            System Name: GS-3510XP
            Serial Number: 4006396720100720
            MAC Address: 00-a0-57-96-48-87
            """.splitlines()
        ]

        minimal_version_output = [
            line.strip() for line in b"""
            Primary Image ----- Version : 4.30.0147RU4
            """.splitlines()
        ]

        # Monkey patch the get method to return minimal outputs
        cliconf.get = MagicMock(side_effect=[
            minimal_system_output,
            minimal_version_output
        ])

        # Call the function
        result = cliconf.get_device_info()

        # Assert that optional fields are not present if not found in output
        assert "network_os_model" not in result
        assert "description" not in result
        assert "manufactured_date" not in result

    def test_get_device_info_failure(self, cliconf):
        # Mock a connection failure for show system command
        cliconf.get = MagicMock(side_effect=Exception("Connection failed"))

        with pytest.raises(AnsibleConnectionFailure) as exc:
            cliconf.get_device_info()

        assert "Failed to retrieve device info: Connection failed" in str(exc.value)
