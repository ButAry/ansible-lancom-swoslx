#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2025 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
author: Heiko Tropartz (@ButAry)
name: swoslx
short_description: Use swoslx cliconf to run command on LANCOM Systems SWOSLX devices.
description:
- This swoslx plugin provides low level abstraction apis for sending and receiving CLI
  commands from LANCOM Systems SWOSLX device.
version_added: 0.1.0
options:
  config_commands:
    description:
    - Specifies a list of commands that can make configuration changes
      to the target device.
    - When `ansible_network_single_user_mode` is enabled, if a command sent
      to the device is present in this list, the existing cache is invalidated.
    version_added: 0.1.0
    type: list
    elements: str
    default: []
    vars:
    - name: ansible_swoslx_config_commands
"""

import re
import json

from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils._text import to_text
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import to_list
from ansible_collections.ansible.netcommon.plugins.plugin_utils.cliconf_base import (
    CliconfBase,
    enable_mode
)

IMAGE_PATTERN = r"Primary Image\s+[-]+\s+Image\s+:\s+(.*)"
VERSION_PATTERN = r"Primary Image\s+[-]+\s+Version\s+:\s+(.*)"
FIRMWARE_PATTERN = r"Primary Image\s+[-]+\s+Upload filename\s+:\s+(.*)"

class Cliconf(CliconfBase):

    terminal_config_prompt = re.compile(br"^.+\(config(-.*)?\)#$")

    def __init__(self, *args, **kwargs):
        super(Cliconf, self).__init__(*args, **kwargs)

    def get_capabilities(self):
        result = super(Cliconf, self).get_capabilities()
        return json.dumps(result)

    def get_device_info(self):
        """
        Parse system information from 'show system' output.
        """
        self.update_cli_prompt_context()

        device_info = {"network_os": "lancom.swoslx"}

        try:
            output = self.get("show system")
            if output and isinstance(output, list):
                output = "\n".join(output)
        except Exception as exc:
            raise AnsibleConnectionFailure(f"Failed to retrieve device 'system' info: {exc}")

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

        try:
            output = self.get("show version")
            if output and isinstance(output, list):
                output = "\n".join(output)
        except Exception as exc:
            raise AnsibleConnectionFailure(f"Failed to retrieve device 'version' info: {exc}")

        image_match = re.search(IMAGE_PATTERN, output)
        version_match = re.search(VERSION_PATTERN, output)
        upload_filename_match = re.search(FIRMWARE_PATTERN, output)

        if image_match:
            device_info["network_os_image"] = image_match.group(1).strip()
        elif version_match:
            device_info["network_os_version"] = version_match.group(1).strip()
        elif upload_filename_match:
            device_info["network_os_platform"] = upload_filename_match.group(1).strip()

        return device_info

    @enable_mode
    def get_config(self, source="running", flags=None, format=None):
        """
        Retrieve the current device configuration.
        Only 'running' is supported.
        """
        if source != "running":
            raise ValueError(f"Fetching configuration from '{source}' is not supported - only 'running")
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
                config = "\n".join(config)
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
        Ensure the command prompt on device is in right mode
        :return: None
        """
        out = self._connection.get_prompt()
        if out is None:
            raise AnsibleConnectionFailure(
                message="cli prompt is not identified from the last received"
                " response window: %s" % self._connection._last_recv_window
            )

        while True:
            out = to_text(out, errors="surrogate_then_replace").strip()
            if out and not self.terminal_config_prompt.match(out):
                self._connection.queue_message("vvvv", "wrong context, sending 'configure' to device")
                self.send_command("configure")
                out = self._connection.get_prompt()
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
                message="cli prompt is not identified from the last received"
                        " response window: %s" % self._connection._last_recv_window
            )

        while True:
            out = to_text(out, errors="surrogate_then_replace").strip()
            if out and self.terminal_config_prompt.match(out):
                self._connection.queue_message("vvvv", "wrong context, sending exit to device")
                self.send_command("exit")
                out = self._connection.get_prompt()
            else:
                break
