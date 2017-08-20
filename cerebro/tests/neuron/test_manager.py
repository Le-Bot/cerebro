import unittest

from cerebro.neuron.manager import AbstractManager, NeuronsManager


class TestNeuronsService(unittest.TestCase):

    def simple_test(*args):
        return "This is dummy neuron"

    KEYWORDS = {"test": simple_test}

    def setUp(self):
        self.obj = NeuronsManager()
        self.obj.add(self.KEYWORDS)
        self.keyword = "test"

    def test_type(self):
        assert isinstance(self.obj, AbstractManager)

    def test_neurons_creation(self):
        assert self.obj.get_all() is not None

    def test_add_neuron(self):
        assert len(self.obj.get_all()) == 1

    def test_is_valid_neuron(self):
        assert self.obj.is_valid(self)

    def test_get_neuron(self):
        assert self.obj.get(self.keyword) is not None

    def test_is_exists_neuron(self):
        assert self.obj.is_exists(self.keyword)

    def test_execute_neuron(self):
        assert self.obj.execute(self.keyword) == "This is dummy neuron"



