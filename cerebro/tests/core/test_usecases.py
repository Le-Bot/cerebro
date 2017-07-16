import unittest

import cerebro.core.usecases as uc


class TestUseCases(unittest.TestCase):
    def setUp(self):
        self.neurons_path = ["./cerebro/tests/neurons"]
        self.neuron_test = "test"

    def test_get_all_neurons(self):
        neurons = uc.get_all_neurons(self.neurons_path)
        assert len(neurons) == 1

    def test_neuron_execution(self):
        neurons = uc.get_all_neurons(self.neurons_path)
        self.assertIsNone(neurons[self.neuron_test]())
