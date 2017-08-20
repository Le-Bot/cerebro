import unittest

import cerebro.neuron as neu


class TestNeuron(unittest.TestCase):
    def setUp(self):
        neu.cfg.add_neurons_location(neu.STR_DEFAULT_NEURONS_PATH)

        self.finder = neu.find

        self.manager = neu.NeuronsManager()

        self.command_args = ("arg1", "arg2")

    def test_neuron_creation(self):
        neuron = neu.Neuron(neu.cfg, self.finder, self.manager)
        assert neuron
        assert neuron.config == neu.cfg
        assert neuron.finder == self.finder
        assert neuron.manager == self.manager

    def test_load_all(self):
        neuron = neu.Neuron(neu.cfg, self.finder, self.manager)
        neuron.load_all()
        assert len(self.manager.get_all()) > 0

    def test_command_execution(self):
        test_keyword = "system check"
        test_response = "All working properly."
        test_command = neu.Command(test_keyword, self.command_args)

        neuron = neu.Neuron(neu.cfg, self.finder, self.manager)
        neuron.load_all()

        response = neuron.process(test_command)
        assert response == test_response

    def test_command_execution_failure(self):
        test_keyword = "wrong command"
        test_command = neu.Command(test_keyword)

        neuron = neu.Neuron(neu.cfg, self.finder, self.manager)
        neuron.load_all()

        response = neuron.process(test_command)
        assert response == neu.STR_DEFAULT_RESPONSE
