# Copyright 2025 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

from unittest.mock import patch

from ansible_collections.lancom.swoslx.plugins.modules import swoslx_hostname
from ansible_collections.lancom.swoslx.tests.unit.modules.utils import set_module_args

from .swoslx_module import TestSwosLxModule


class TestSwosLxHostnameModule(TestSwosLxModule):
    module = swoslx_hostname

    def setUp(self):
        super(TestSwosLxHostnameModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection"
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.lancom.swoslx.plugins.module_utils.network.swoslx.facts.hostname.hostname.HostnameFacts.get_config"
        )
        self.execute_show_command = self.mock_execute_show_command.start()
        self.execute_show_command.return_value = "hostname swoslx_test"

    def tearDown(self):
        super(TestSwosLxHostnameModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_execute_show_command.stop()

    def test_swoslx_hostname_merged_idempotent(self):
        set_module_args(dict(config=dict(hostname="swoslx_test"), state="merged"))
        self.execute_module(changed=False, commands=[])

    def test_swoslx_hostname_replaced_idempotent(self):
        set_module_args(dict(config=dict(hostname="swoslx_test"), state="replaced"))
        self.execute_module(changed=False, commands=[])

    def test_swoslx_hostname_overridden_idempotent(self):
        set_module_args(dict(config=dict(hostname="swoslx_test"), state="overridden"))
        self.execute_module(changed=False, commands=[])

    def test_swoslx_hostname_merged(self):
        set_module_args(dict(config=dict(hostname="swoslx_new"), state="merged"))
        self.execute_module(changed=True, commands=["hostname swoslx_new"])

    def test_swoslx_hostname_replaced(self):
        set_module_args(dict(config=dict(hostname="swoslx_new"), state="replaced"))
        self.execute_module(changed=True, commands=["hostname swoslx_new"])

    def test_swoslx_hostname_overridden(self):
        set_module_args(dict(config=dict(hostname="swoslx_new"), state="overridden"))
        self.execute_module(changed=True, commands=["hostname swoslx_new"])

    def test_swoslx_hostname_deleted(self):
        set_module_args(dict(config=dict(), state="deleted"))
        self.execute_module(changed=True, commands=["no hostname swoslx_test"])

    def test_swoslx_hostname_gathered(self):
        set_module_args(dict(config=dict(), state="gathered"))
        result = self.execute_module(changed=False)
        gathered_list = {"hostname": "swoslx_test"}
        self.assertEqual(sorted(gathered_list), sorted(result["gathered"]))

    def test_swoslx_hostname_parsed(self):
        parsed_str = "hostname swoslx_test"
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = {"hostname": "swoslx_test"}
        self.assertEqual(sorted(parsed_list), sorted(result["parsed"]))

    def test_swoslx_hostname_rendered(self):
        set_module_args(
            dict(state="rendered", config=dict(hostname="swoslx_test"))
        )
        commands = ["hostname swoslx_test"]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(commands),
            result["rendered"]
        )
