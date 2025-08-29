import pytest
import json
import re

from unittest.mock import MagicMock, call
from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils._text import to_bytes, to_text

from ansible_collections.lancom.swoslx.plugins.terminal.swoslx import TerminalModule

DISABLED_OUTPUT = b"GS-3510XP>"
ENABLED_OUTPUT = b"GS-3510XP#"
CONFIGURED_OUTPUT = b"GS-3510XP(config)#"

class TestTerminalModule:
    @pytest.fixture
    def terminal_module(self):
        plugin = TerminalModule(connection=MagicMock())
        plugin._exec_cli_command = MagicMock()
        plugin._get_prompt = MagicMock()
        return plugin

    """
    terminal on_open
    """

    def test_on_open_shell_expect_terminal_commands(self, terminal_module):
        terminal_module.on_open_shell()
        assert terminal_module._exec_cli_command.call_args_list == [
            call(b"terminal length 0"),
            call(b"terminal width 512")
        ]

    """
    terminal on_become
    """

    def test_on_become_already_in_privileged_mode(self, terminal_module):
        terminal_module._get_prompt.return_value = CONFIGURED_OUTPUT
        terminal_module.on_become()
        terminal_module._exec_cli_command.assert_not_called()

    def test_on_become_not_in_privileged_mode_no_password(self, terminal_module):
        terminal_module._get_prompt.side_effect = [DISABLED_OUTPUT, CONFIGURED_OUTPUT]
        terminal_module.on_become()
        terminal_module._exec_cli_command.assert_called_once_with(b'{"command": "enable"}')

    def test_on_become_not_in_privileged_mode_with_password(self, terminal_module):
        password = "secret123\\1a"
        terminal_module._get_prompt.side_effect = [DISABLED_OUTPUT, CONFIGURED_OUTPUT]
        terminal_module.on_become(passwd=password)
        assert terminal_module._exec_cli_command.call_args == call(to_bytes(json.dumps({
            "command": "enable",
            "prompt": "[\r\n]?[Pp]assword: $",
            "answer": password,
            "prompt_retry_check": "True"
        }), errors="surrogate_or_strict"))

    def test_on_become_fails_to_enter_privileged_mode(self, terminal_module):
        terminal_module._get_prompt.return_value = DISABLED_OUTPUT
        terminal_module._exec_cli_command.side_effect = AnsibleConnectionFailure("unknown error")
        with pytest.raises(AnsibleConnectionFailure,
                           match=re.escape("Failed to enable privileged user mode at prompt [GS-3510XP>] with error: unknown error")):
            terminal_module.on_become()

    def test_on_become_fails_to_change_prompt_after_enable(self, terminal_module):
        terminal_module._get_prompt.side_effect = [DISABLED_OUTPUT, DISABLED_OUTPUT]
        with pytest.raises(AnsibleConnectionFailure,
                           match=re.escape("Failed to enable privileged user mode, still at prompt [GS-3510XP>]")):
            terminal_module.on_become()

    """
    terminal on_unbecome
    """

    def test_on_unbecome_not_in_privileged_mode(self, terminal_module):
        terminal_module._get_prompt.return_value = DISABLED_OUTPUT
        terminal_module.on_unbecome()
        terminal_module._exec_cli_command.assert_not_called()

    def test_on_unbecome_in_privileged_not_config_mode(self, terminal_module):
        terminal_module._get_prompt.side_effect = [ENABLED_OUTPUT, DISABLED_OUTPUT]
        terminal_module.on_unbecome()
        assert terminal_module._exec_cli_command.call_args_list == [call(b"disable")]

    def test_on_unbecome_in_privileged_in_config_mode(self, terminal_module):
        terminal_module._get_prompt.side_effect = [CONFIGURED_OUTPUT, DISABLED_OUTPUT]
        terminal_module.on_unbecome()
        assert terminal_module._exec_cli_command.call_args_list == [
            call(b"exit"),
            call(b"disable")
        ]

    def test_on_unbecome_disable_fails(self, terminal_module):
        terminal_module._get_prompt.return_value = ENABLED_OUTPUT
        terminal_module._exec_cli_command.side_effect = AnsibleConnectionFailure("disable error")
        with pytest.raises(AnsibleConnectionFailure,
                           match=re.escape("Failed to disable privileged user mode with error: disable error")):
            terminal_module.on_unbecome()

    def test_on_unbecome_prompt_still_privileged(self, terminal_module):
        terminal_module._get_prompt.side_effect = [ENABLED_OUTPUT, ENABLED_OUTPUT]
        with pytest.raises(AnsibleConnectionFailure,
                           match=re.escape("Failed to disable privileged user mode, still at prompt [GS-3510XP#]")):
            terminal_module.on_unbecome()
