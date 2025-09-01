import pytest

from unittest.mock import MagicMock, call
from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils._text import to_text
from ansible_collections.lancom.swoslx.plugins.cliconf.swoslx import Cliconf
from .fixtures import system_output, version_output, running_config

ENABLED_OUTPUT = b"GS-3510XP#"
CONFIGURED_OUTPUT = b"GS-3510XP(config)#"

class TestCliconf:
    @pytest.fixture
    def cliconf(self):
        connection = MagicMock()
        connection.get_prompt.return_value = ENABLED_OUTPUT

        plugin = Cliconf(connection=connection)
        plugin.set_cli_prompt_context = MagicMock()
        plugin.update_cli_prompt_context = MagicMock()
        plugin.run_commands = MagicMock()

        return plugin

    def test_get_device_info_successful(self, cliconf, system_output, version_output):
        system_lines = [line.strip() for line in system_output.splitlines()]
        version_lines = [line.strip() for line in version_output.splitlines()]

        cliconf.get = MagicMock(side_effect=[
            system_lines,   # First call for 'show system'
            version_lines   # Second call for 'show version'
        ])

        result = cliconf.get_device_info()

        cliconf.get.assert_has_calls([
            call('show system'),
            call('show version')
        ])

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

        cliconf._connection._get_prompt.return_value = ENABLED_OUTPUT
        cliconf.get = MagicMock(side_effect=[
            minimal_system_output,
            minimal_version_output
        ])

        result = cliconf.get_device_info()

        cliconf.get.assert_has_calls([
            call('show system'),
            call('show version')
        ])

        assert "network_os_model" not in result
        assert "description" not in result
        assert "manufactured_date" not in result

    def test_get_device_info_failure(self, cliconf):
        cliconf.get = MagicMock(side_effect=Exception("Connection failed"))

        with pytest.raises(AnsibleConnectionFailure) as exc:
            cliconf.get_device_info()

        assert "Failed to retrieve device info: Connection failed" in str(exc.value)

    def test_get_config_successful(self, cliconf, running_config):
        cliconf.get = MagicMock(return_value=running_config)
        result = cliconf.get_config(source="running")
        cliconf.get.assert_has_calls([
            call('show running-config all-defaults')
        ])

        assert to_text(result) == to_text(running_config)

    def test_get_config_with_flags(self, cliconf, running_config):
        running_config_flagged = b"""
            automatic-firmware-update Check-Time-Begin 0
            automatic-firmware-update Check-Time-End 0
            """

        cliconf.get = MagicMock(return_value=running_config_flagged)
        result = cliconf.get_config(source="running", flags=["automatic-firmware-update", "Check-Time"])
        result = to_text(result)

        cliconf.get.assert_has_calls([
            call('show running-config all-defaults | include automatic-firmware-update Check-Time')
        ])

        assert to_text(result) == to_text(running_config_flagged)

    def test_get_config_invalid_source(self, cliconf):
        with pytest.raises(ValueError) as exc:
            cliconf.get_config(source="startup")

        assert "Fetching configuration from 'startup' is not supported - only 'running'" in str(exc.value)

    def test_get_config_with_format(self, cliconf):
        with pytest.raises(ValueError) as exc:
            cliconf.get_config(source="running", format="json")

        assert "Configuration output 'format' is not supported" in str(exc.value)

    def test_edit_config_successful(self, cliconf):
        cliconf.run_commands = MagicMock(return_value="Commands applied")
        cliconf._connection._get_prompt.side_effect = [CONFIGURED_OUTPUT, ENABLED_OUTPUT]

        candidate = "logging on"
        result = cliconf.edit_config(candidate=candidate)

        cliconf.set_cli_prompt_context.assert_called_once()
        cliconf.run_commands.assert_called_once_with(candidate)
        cliconf.update_cli_prompt_context.assert_called_once()

        assert result == "Commands applied"

    def test_edit_config_empty_candidate(self, cliconf):
        result = cliconf.edit_config(candidate=[])
        cliconf.set_cli_prompt_context.assert_not_called()
        cliconf.run_commands.assert_not_called()
        assert result == ""

    def test_edit_config_failure(self, cliconf, running_config):
        candidate = "logging on"
        cliconf.run_commands = MagicMock(side_effect=Exception("Command failed"))
        with pytest.raises(Exception) as exc:
            cliconf.edit_config(candidate=candidate)
        assert str(exc.value) == "Command failed"

    def test_edit_config_set_prompt_failure(self, cliconf, running_config):
        candidate = "logging on"
        cliconf.set_cli_prompt_context = MagicMock(
            side_effect=AnsibleConnectionFailure("Failed to set prompt context")
        )
        with pytest.raises(AnsibleConnectionFailure) as exc:
            cliconf.edit_config(candidate=candidate)
        assert "Failed to set prompt context" in str(exc.value)

    def test_edit_config_update_prompt_failure(self, cliconf, running_config):
        candidate = "logging on"
        cliconf.update_cli_prompt_context = MagicMock(
            side_effect=AnsibleConnectionFailure("Failed to update prompt context")
        )
        with pytest.raises(AnsibleConnectionFailure) as exc:
            cliconf.edit_config(candidate=candidate)
        assert "Failed to update prompt context" in str(exc.value)
