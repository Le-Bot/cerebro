import unittest

import cerebro.neuron as neu


class TestConfigService(unittest.TestCase):
    def test_config_creation(self):
        assert neu.cfg.get_neurons_path() is not None

    def test_add_path(self):
        neu.cfg.add_neurons_location(neu.STR_DEFAULT_NEURONS_PATH)
        assert len(neu.cfg.get_neurons_path()) == 1
