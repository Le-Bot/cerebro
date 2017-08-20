import unittest

import cerebro.neuron  as neu


class TestFinder(unittest.TestCase):

    def test_find_neurons(self):
        neu.cfg.add_neurons_location(neu.STR_DEFAULT_NEURONS_PATH)
        assert neu.find(neu.cfg.get_neurons_path()) is not None
