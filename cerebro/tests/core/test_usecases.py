import unittest

import cerebro.core.entities as en
import cerebro.core.usecases as uc


class TestUseCases(unittest.TestCase):
    def setUp(self):
        self.neurons_path = ["./cerebro/tests/neurons"]
        self.neuron_test = ("test")
        self.neuron_test_response = "This is test neuron"
        self.command_args = ("arg1", "arg2")

        uc.get_all_neurons(self.neurons_path)

        self.test_command = en.Command(self.neuron_test, self.command_args)

    def test_get_all_neurons(self):
        assert len(uc.NEURONS) == 1

    def test_neuron_execution(self):
        assert uc.NEURONS[self.neuron_test]() == self.neuron_test_response

    def test_command_execution(self):
        response = uc.process_command(self.test_command)
        assert response == self.neuron_test_response
