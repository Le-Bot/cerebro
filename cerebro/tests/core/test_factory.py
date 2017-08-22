import unittest

import cerebro.neuron.neuron as neu
import cerebro.nlp.nlp as n
import cerebro.core.factory as fact


class TestFactory(unittest.TestCase):

    def setUp(self):
        self.obj = fact.DefaultFactory()

    def test_type(self):
        self.assertIsInstance(self.obj, fact.BaseFactory)

    def test_creation(self):
        self.assertIsNotNone(self.obj)

    def test_neuron(self):
        neuron = self.obj.neuron()
        self.assertIsInstance(neuron, neu.Neuron)

    def test_nlp(self):
        nlp = self.obj.nlp()
        self.assertIsInstance(nlp, n.NLP)

    def test_cerebro(self):
        nlp, neuron = self.obj.cerebro()
        self.assertIsInstance(nlp, n.NLP)
        self.assertIsInstance(neuron, neu.Neuron)