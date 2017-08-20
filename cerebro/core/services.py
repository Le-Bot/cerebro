import abc
import pkgutil

import constants as const


class AbstractNeuronsService(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_all(self):
        return

    @abc.abstractmethod
    def add(self, obj):
        pass

    @abc.abstractmethod
    def is_valid(self, neuron):
        return

    @abc.abstractmethod
    def get(self, keyword):
        return

    @abc.abstractmethod
    def is_exists(self, keyword):
        return

    @abc.abstractmethod
    def execute(self, keyword, args=None):
        return


class NeuronsService(AbstractNeuronsService):
    def __init__(self):
        self.neurons = {}

    def get_all(self):
        return self.neurons

    def add(self, obj):
        self.neurons.update(obj)

    def is_valid(self, neuron):
        return hasattr(neuron, const.STR_KEYWORDS)

    def get(self, keyword):
        return self.neurons.get(keyword)

    def is_exists(self, keyword):
        return self.neurons.has_key(keyword)

    def execute(self, keyword, args=None):
        return self.get(keyword)(args) if self.is_exists(keyword) else const.STR_DEFAULT_RESPONSE


def find_neurons(path):
    for finder, name, is_pkg in pkgutil.walk_packages(path):
        loader = finder.find_module(name)
        mod = loader.load_module(name)
        yield mod
