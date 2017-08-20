import unittest

import cerebro.neuron as neu


class TestUseCases(unittest.TestCase):
    def setUp(self):
        neu.cfg.add_neurons_location(neu.STR_DEFAULT_NEURONS_PATH)

        self.finder = neu.find

        self.manager = neu.NeuronsManager()

        self.command_args = ("arg1", "arg2")

    def test_cerebro_creation(self):
        cerebro = neu.Neuron(neu.cfg, self.finder, self.manager)
        assert cerebro
        assert cerebro.config == neu.cfg
        assert cerebro.finder == self.finder
        assert cerebro.manager == self.manager

    def test_load_all_neurons(self):
        cerebro = neu.Neuron(neu.cfg, self.finder, self.manager)
        cerebro.load_all_neurons()
        assert len(self.manager.get_all()) > 0

    def test_command_execution(self):
        test_keyword = "system check"
        test_response = "All working properly."
        test_command = neu.Command(test_keyword, self.command_args)

        cerebro = neu.Neuron(neu.cfg, self.finder, self.manager)
        cerebro.load_all_neurons()

        response = cerebro.process_command(test_command)
        assert response == test_response

    def test_command_execution_failure(self):
        test_keyword = "wrong command"
        test_command = neu.Command(test_keyword)

        cerebro = neu.Neuron(neu.cfg, self.finder, self.manager)
        cerebro.load_all_neurons()

        response = cerebro.process_command(test_command)
        assert response == neu.STR_DEFAULT_RESPONSE
