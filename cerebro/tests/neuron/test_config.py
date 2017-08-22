import unittest

import cerebro.neuron as neu


class TestConfig(unittest.TestCase):
    def test_config_creation(self):
        self.assertIsNotNone(neu.cfg.get_neurons_path())

    def test_add_path(self):
        neu.cfg.add_neurons_location(neu.STR_DEFAULT_NEURONS_PATH)
        self.assertNotEquals(len(neu.cfg.get_neurons_path()), 0)
