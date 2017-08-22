import unittest

import cerebro.data.neurons.simple as sim


class TestSimple(unittest.TestCase):

    def setUp(self):
        self.response = "All working properly."
        self.keyword = "greet"
        self.valid_attr = "KEYWORDS"

    def test_valid(self):
        self.assertTrue(hasattr(sim, self.valid_attr))

    def test_simple(self):
        self.assertEqual(sim.simple_test(), self.response)

    def test_neuron(self):
        self.assertEqual(sim.KEYWORDS[self.keyword](), self.response)
