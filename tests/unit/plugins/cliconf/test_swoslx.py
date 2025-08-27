import pytest
import json
import re

from unittest.mock import MagicMock, call
from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils._text import to_bytes, to_text

from ansible_collections.lancom.swoslx.plugins.cliconf.swoslx import Cliconf

class TestCliconf:
    @pytest.fixture
    def cliconf(self):
        plugin = Cliconf()
        return plugin
