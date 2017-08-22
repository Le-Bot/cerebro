import abc

import constants as const


class AbstractManager(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_all(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def add(self, obj):
        raise NotImplementedError()

    @abc.abstractmethod
    def is_valid(self, neuron):
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, keyword):
        raise NotImplementedError()

    @abc.abstractmethod
    def is_exists(self, keyword):
        raise NotImplementedError()

    @abc.abstractmethod
    def execute(self, keyword, args=None):
        raise NotImplementedError()


class NeuronsManager(AbstractManager):
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



