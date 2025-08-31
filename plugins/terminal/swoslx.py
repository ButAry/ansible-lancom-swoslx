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
short_description: Use swoslx terminal to run command on LANCOM Systems SWOSLX devices.
description:
- This plugin is an Ansible terminal plugin that provides an interface for executing
  commands in a terminal environment. It allows users to open a shell session, run
  commands, and manage the terminal state.
version_added: 0.1.0

Usage:
    This plugin can be used in Ansible playbooks to interact with devices or
    systems that require command-line interface (CLI) access. Users can define
    tasks that utilize this plugin to run commands and retrieve results.

Example:
    - name: Run command using MyTerminalPlugin
      lancom.swoslx:
        command: "show history"
"""

import json
import re

from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils._text import to_bytes, to_text
from ansible_collections.ansible.netcommon.plugins.plugin_utils.terminal_base import TerminalBase

class TerminalModule(TerminalBase):
    def __init__(self, *args, **kwargs):
        super(TerminalModule, self).__init__(*args, **kwargs)

    terminal_config_prompt_re = re.compile(br"^.+\(config(-.*)?\)#$")

    terminal_stdout_re = [
        re.compile(br"[\r\n]?[\w+\-.:/\[\]]+(?:\([^)]+\)){0,3}[>#] ?$"),
    ]

    terminal_stderr_re = [
        re.compile(br"% Incomplete command."),
        re.compile(br"% Invalid word detected at '\^' marker."),
        re.compile(br"% No password set")
    ]

    def on_open_shell(self):
        """
        Called after the SSH session is established

        This method is called right after the invoke_shell() is called from
        the Paramiko SSHClient instance.  It provides an opportunity to set up
        terminal parameters such as disabling paging for instance.
        """
        try:
            for cmd in (b"terminal length 0", b"terminal width 512"):
                self._exec_cli_command(cmd)
        except Exception as e:
            raise AnsibleConnectionFailure(f"Failed to set terminal parameters with error: {e}")

    def on_become(self, passwd=None):
        """
        Called when privilege escalation is requested

        kwarg passwd: String containing the password

        This method is called when the privilege is requested to be elevated
        in the play context by setting become to True.  It is the responsibility
        of the terminal plugin to actually do the privilege escalation such
        as entering `enable` mode for instance
        """
        prompt = self._get_prompt()
        if prompt is None or prompt.endswith(b"#"):
            return # if prompt is undefined or already in privileged mode, do nothing

        cmd = {"command": "enable"}
        if passwd:
            cmd["prompt"] = "[\r\n]?[Pp]assword: $"
            cmd["answer"] = to_text(passwd, errors="surrogate_or_strict")
            cmd["prompt_retry_check"] = "True"

        try:
            self._exec_cli_command(to_bytes(json.dumps(cmd), errors="surrogate_or_strict"))
        except Exception as e:
            raise AnsibleConnectionFailure(f"Failed to enable privileged user mode at prompt [{to_text(prompt)}] with error: {e}")

        prompt = self._get_prompt()
        if prompt is None or not prompt.endswith(b"#"):
            raise AnsibleConnectionFailure(f"Failed to enable privileged user mode, still at prompt [{to_text(prompt)}]")

    def on_unbecome(self):
        """
        Called when privilege deescalation is requested

        This method is called when the privilege changed from escalated
        (become=True) to non escalated (become=False).  It is the responsibility
        of this method to actually perform the deauthorization procedure
        """
        prompt = self._get_prompt()
        if prompt is None or not prompt.endswith(b"#"):
            return # if prompt is undefined or not in privileged mode, do nothing

        try:
            if self.terminal_config_prompt_re.match(prompt):
                self._exec_cli_command(b"exit")

            self._exec_cli_command(b"disable")
        except AnsibleConnectionFailure as e:
            raise AnsibleConnectionFailure(f"Failed to disable privileged user mode with error: {e}")

        prompt = self._get_prompt()
        if prompt is None or prompt.endswith(b"#"):
            raise AnsibleConnectionFailure(f"Failed to disable privileged user mode, still at prompt [{to_text(prompt)}]")
