import unittest

import cerebro.core.entities as en
import cerebro.core.usecases as uc
import cerebro.core.services as ser


class TestConfigService(unittest.TestCase):

    def setUp(self):
        self.obj = ser.ConfigService()

    def test_config_creation(self):
        assert self.obj.get_neurons_path() is not None

    def test_add_path(self):
        self.obj.add_neurons_location("./cerebro/neurons")
        assert len(self.obj.get_neurons_path()) == 1

