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
        self.assertIsNotNone(neuron)
        self.assertEqual(neuron.config, neu.cfg)
        self.assertEqual(neuron.finder, self.finder)
        self.assertEqual(neuron.manager, self.manager)

    def test_load_all(self):
        neuron = neu.Neuron(neu.cfg, self.finder, self.manager)
        neuron.load_all()
        self.assertGreater(len(self.manager.get_all()), 0)

    def test_command_execution(self):
        test_keyword = "greet"
        test_response = "All working properly."
        test_command = neu.Command(test_keyword, self.command_args)

        neuron = neu.Neuron(neu.cfg, self.finder, self.manager)
        neuron.load_all()

        response = neuron.process(test_command)
        self.assertEqual(response, test_response)

    def test_command_execution_failure(self):
        test_keyword = "wrong command"
        test_command = neu.Command(test_keyword)

        neuron = neu.Neuron(neu.cfg, self.finder, self.manager)
        neuron.load_all()

        response = neuron.process(test_command)
        self.assertEqual(response, neu.STR_DEFAULT_RESPONSE)
