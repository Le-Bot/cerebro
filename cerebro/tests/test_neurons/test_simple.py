import unittest

import cerebro.data.neurons.simple as sim


class TestSimple(unittest.TestCase):

    def setUp(self):
        self.response = "All working properly."
        self.keyword = "system check"
        self.valid_attr = "KEYWORDS"

    def test_valid(self):
        assert hasattr(sim, self.valid_attr)

    def test_simple(self):
        assert sim.simple_test() == self.response

    def test_neuron(self):
        assert sim.KEYWORDS[self.keyword]() == self.response
