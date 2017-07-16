import unittest

import cerebro.core.usecases as uc


class TestUseCases(unittest.TestCase):
    def setUp(self):
        self.neurons_path = ["./cerebro/tests/neurons"]
        self.neuron_test = "test"
        self.neuron_test_response = "This is test neuron"
        uc.get_all_neurons(self.neurons_path)

    def test_get_all_neurons(self):
        neurons = uc.NEURONS
        assert len(neurons) == 1

    def test_neuron_execution(self):
        neurons = uc.NEURONS
        assert neurons[self.neuron_test]() == self.neuron_test_response