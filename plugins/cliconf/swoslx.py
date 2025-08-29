import re
import json

from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils._text import to_text, to_bytes
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import to_list
from ansible_collections.ansible.netcommon.plugins.plugin_utils.cliconf_base import (
    CliconfBase,
    enable_mode
)

VERSION_PATTERN = re.compile(r"(?ms)^Primary Image\b.*?^\s*Version\s*:\s*(\S+)")
FIRMWARE_PATTERN = re.compile(r"(?ms)^Primary Image\b.*?^\s*Upload filename\s*:\s*(\S+)")

class Cliconf(CliconfBase):
    terminal_config_prompt = re.compile(r"^.+\(config(-.*)?\)#$")

    def __init__(self, *args, **kwargs):
        super(Cliconf, self).__init__(*args, **kwargs)

    def get_capabilities(self):
        result = super(Cliconf, self).get_capabilities()
        return json.dumps(result)

    def get_device_info(self):
        """
        Parse system information from 'show system' and 'show version' output.
        """
        self.update_cli_prompt_context()

        device_info = {"network_os": "lancom.swoslx"}

        try:
            # Get system info
            output = self.get("show system")
            if isinstance(output, list):
                output = "\n".join(to_text(line) for line in output)
            
            for line in output.splitlines():
                line = line.strip()
                if line.startswith("Model Name"):
                    device_info["network_os_model"] = line.split(":", 1)[1].strip()
                elif line.startswith("System Description"):
                    device_info["description"] = line.split(":", 1)[1].strip()
                elif line.startswith("System Name"):
                    device_info["network_os_hostname"] = line.split(":", 1)[1].strip()
                elif line.startswith("Serial Number"):
                    device_info["serial_number"] = line.split(":", 1)[1].strip()
                elif line.startswith("MAC Address"):
                    device_info["macaddress"] = line.split(":", 1)[1].strip()
                elif line.startswith("Production Date"):
                    device_info["manufactured_date"] = line.split(":", 1)[1].strip()

            # Get version info
            output = self.get("show version")
            print(f"# output: {output}")
            if isinstance(output, list):
                output = "\n".join(to_text(line) for line in output)

            version_match = VERSION_PATTERN.search(output)
            firmware_match = FIRMWARE_PATTERN.search(output)

            if version_match:
                device_info["network_os_version"] = version_match.group(1).strip()
            if firmware_match:
                device_info["network_os_image"] = firmware_match.group(1).strip()

        except Exception as exc:
            raise AnsibleConnectionFailure(f"Failed to retrieve device info: {exc}")

        return device_info

    @enable_mode
    def get_config(self, source="running", flags=None, format=None):
        """
        Retrieve the current device configuration.
          source: only 'running' configuration supported.
          flags: list of config parameter/key names to include.
                 Example-1:
                 ```
                     filter: automatic-firmware-update
                     output: automatic-firmware-update Mode check-and-update
                             automatic-firmware-update Version-Policy security-updates-only
                             automatic-firmware-update Check-Interval daily
                             automatic-firmware-update Base-Url update.lancom-systems.de
                             automatic-firmware-update Check-Time-Begin 0
                             automatic-firmware-update Check-Time-End 0
                             automatic-firmware-update Install-Time-Begin 2
                             automatic-firmware-update Install-Time-End 4
                 ```
                Example-2:
                 ```
                    filter: Check-Interval
                    output: automatic-firmware-update Check-Interval daily
                ```
        """
        if source != "running":
            raise ValueError(f"Fetching configuration from '{source}' is not supported - only 'running'")
        if format:
            raise ValueError("Configuration output 'format' is not supported")

        self.update_cli_prompt_context()

        cmd = "show running-config all-defaults"

        if flags:
            cmd += " | include"
            cmd += " ".join(to_list(flags))
            cmd = cmd.strip()

        try:
            config = self.get(cmd)
            if isinstance(config, list):
                config = "\n".join(to_text(line) for line in config)
            return config
        except Exception as exc:
            raise AnsibleConnectionFailure(f"Failed to retrieve running configuration: {exc}")

    @enable_mode
    def edit_config(self, candidate=None, commit=True, replace=None, diff=False, comment=None):
        """
        Apply configuration to the device using CLI commands.
        :param candidate: list of configuration lines to apply
        :param commit: ignored, config is applied immediately
        :param replace: ignored, swoslx does not support replace
        :param comment: optional comment (not used here)
        """
        if not candidate:
            return ""

        self.set_cli_prompt_context()
        response = self.run_commands(candidate)
        self.update_cli_prompt_context()
        return response

    def set_cli_prompt_context(self):
        """
        Ensure the command prompt on device is in the correct mode
        :return: None
        """
        out = self._connection.get_prompt()

        if out is None:
            raise AnsibleConnectionFailure(
                message="cli prompt is not identified from the last received response window: %s" % 
                       self._connection._last_recv_window
            )

        while True:
            out = to_text(out, errors="surrogate_then_replace").strip()
            if self.terminal_config_prompt.match(out):
                break
            else:
                if out and not self.terminal_config_prompt.match(out):
                    self._connection.queue_message("vvvv", "wrong context, sending 'configure' to device")
                    self.send_command("configure")
                else:
                    break

    def update_cli_prompt_context(self):
        """
        Update the cli prompt context to ensure it is in operational mode
        :return: None
        """
        out = self._connection.get_prompt()

        if out is None:
            raise AnsibleConnectionFailure(
                message="cli prompt is not identified from the last received response window: %s" % 
                       self._connection._last_recv_window
            )

        while True:
            out = to_text(out, errors="surrogate_then_replace").strip()
            if self.terminal_config_prompt.match(out):
                break
            else:
                if out and self.terminal_config_prompt.match(out):
                    self._connection.queue_message("vvvv", "wrong context, sending exit to device")
                    self.send_command("exit")
                else:
                    break
