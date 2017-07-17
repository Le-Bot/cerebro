import unittest

import cerebro.core.entities as en
import cerebro.core.usecases as uc
import cerebro.core.services as ser


class TestConfigService(unittest.TestCase):
    def setUp(self):
        self.obj = ser.ConfigService()

    def test_config_creation(self):
        assert self.obj.get_neurons_path() is not None

    def test_add_path(self):
        self.obj.add_neurons_location("./cerebro/neurons")
        assert len(self.obj.get_neurons_path()) == 1


class TestNeuronsService(unittest.TestCase):

    def simple_test(*args):
        return "This is dummy neuron"

    KEYWORDS = {
            ("test"): simple_test
        }

    def setUp(self):
        self.obj = ser.NeuronsService()
        self.obj.add_neuron(self.KEYWORDS)

    def test_neurons_creation(self):
        assert self.obj.get_all_neurons() is not None

    def test_add_neuron(self):
        assert len(self.obj.get_all_neurons()) == 1

    def test_is_valid_neuron(self):
        assert self.obj.is_valid_neuron(self)

    def test_get_neuron(self):
        assert self.obj.get_neuron("test") is not None

    def test_is_exists_neuron(self):
        assert self.obj.is_exists_neuron("test")

    def test_execute_neuron(self):
        assert self.obj.execute_neuron("test") == "This is dummy neuron"

