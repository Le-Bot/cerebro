import unittest

from cerebro.neuron.manager import AbstractManager, NeuronsManager


def simple_neuron(*args):
    return "This is dummy neuron"


class TestManager(unittest.TestCase):

    KEYWORDS = {"test": simple_neuron}

    def setUp(self):
        self.obj = NeuronsManager()
        self.obj.add(self.KEYWORDS)
        self.keyword = "test"

    def test_type(self):
        self.assertIsInstance(self.obj, AbstractManager)

    def test_neurons_creation(self):
        self.assertIsNotNone(self.obj.get_all())

    def test_add_neuron(self):
        self.assertEquals(len(self.obj.get_all()), 1)

    def test_is_valid_neuron(self):
        self.assertTrue(self.obj.is_valid(self))

    def test_get_neuron(self):
        self.assertIsNotNone(self.obj.get(self.keyword))

    def test_is_exists_neuron(self):
        self.assertTrue(self.obj.is_exists(self.keyword))

    def test_execute_neuron(self):
        self.assertEquals(self.obj.execute(self.keyword), "This is dummy neuron")



