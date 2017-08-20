import abc
import pkgutil

import constants as const


class AbstractConfigService(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def add_neurons_location(self, path):
        return

    @abc.abstractmethod
    def get_neurons_path(self):
        return


class AbstractNeuronsFinderService(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def find_neurons(self, path):
        return


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


class ConfigService(AbstractConfigService):
    def __init__(self):
        self.__neurons_path = []

    def add_neurons_location(self, path):
        self.__neurons_path.append(path)

    def get_neurons_path(self):
        return self.__neurons_path


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


class NeuronsFinderService(AbstractNeuronsFinderService):
    def find_neurons(self, path):
        for finder, name, is_pkg in pkgutil.walk_packages(path):
            loader = finder.find_module(name)
            mod = loader.load_module(name)
            yield mod
