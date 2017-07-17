import unittest

import cerebro.core.entities as en
import cerebro.core.usecases as uc


class TestUseCases(unittest.TestCase):
    def setUp(self):
        self.neurons_path = ["./cerebro/neurons"]

        self.neuron_test = ("system check")
        self.neuron_test_response = "All working properly."
        self.command_args = ("arg1", "arg2")
        self.test_command = en.Command(self.neuron_test, self.command_args)

        self.total_neurons = 2
        uc.get_all_neurons(self.neurons_path)

    def test_get_all_neurons(self):
        assert len(uc.NEURONS) == self.total_neurons

    def test_neuron_execution(self):
        assert uc.NEURONS[self.neuron_test]() == self.neuron_test_response

    def test_command_execution(self):
        response = uc.process_command(self.test_command)
        assert response == self.neuron_test_response

    def test_command_execution_faliure(self):
        error_test = ("asd asdasd ")
        error_test_response = "Sorry, I could not process that."
        error_command = en.Command(error_test, self.command_args)

        response = uc.process_command(error_command)
        assert response == error_test_response