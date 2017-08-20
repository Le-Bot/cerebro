import unittest

from cerebro.neuron import constants as const, config as cfg, finder as fn


class TestNeuronsFinderService(unittest.TestCase):

    def test_find_neurons(self):
        cfg.add_neurons_location(const.STR_DEFAULT_NEURONS_PATH)
        assert fn.find(cfg.get_neurons_path()) is not None
