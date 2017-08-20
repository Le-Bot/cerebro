import unittest

import cerebro.core.config as cfg
import cerebro.core.constants as const


class TestConfigService(unittest.TestCase):
    def test_config_creation(self):
        assert cfg.get_neurons_path() is not None

    def test_add_path(self):
        cfg.add_neurons_location(const.STR_DEFAULT_NEURONS_PATH)
        assert len(cfg.get_neurons_path()) == 1
