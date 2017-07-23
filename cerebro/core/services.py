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
    __metaclass__ =  abc.ABCMeta

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
    def get(self, keywords):
        return

    @abc.abstractmethod
    def is_exists(self, keywords):
        return

    @abc.abstractmethod
    def execute(self, keywords, args=None):
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

    def get(self, keywords):
        flag = None
        for key, value in self.neurons.iteritems():
            keywords_set = set(keywords)
            key_set = set(key)
            if key_set == keywords_set or key_set.intersection(keywords_set):
                flag = value
                break
        return flag

    def is_exists(self, keywords):
        flag = False
        for key in self.neurons.iterkeys():
            keywords_set = set(keywords)
            key_set = set(key)
            if key_set == keywords_set or key_set.intersection(keywords_set):
                flag = True
                break
        return flag

    def execute(self, keywords, args=None):
        return self.get(keywords)(args) if self.is_exists(keywords) else None


class NeuronsFinderService(AbstractNeuronsFinderService):
    def find_neurons(self, path):
        modules = []
        for finder, name, is_pkg in pkgutil.walk_packages(path):
            try:

                loader = finder.find_module(name)
                mod = loader.load_module(name)
                modules.append(mod)
            except:
                print("Error loading '%s'".format(name))

        return modules
