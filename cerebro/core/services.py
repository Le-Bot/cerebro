import constants as const


class ConfigService(object):
    def __init__(self):
        self.__neurons_path = []

    def add_neurons_location(self, path):
        self.__neurons_path.append(path)

    def get_neurons_path(self):
        return self.__neurons_path


class NeuronsService(object):
    def __init__(self):
        self.neurons = {}

    def get_all(self):
        return self.neurons

    def add(self, obj):
        self.neurons.update(obj)

    @staticmethod
    def is_valid(neuron):
        return hasattr(neuron, const.STR_KEYWORDS)

    def get(self, keywords):
        return self.neurons.get(keywords, None)

    def is_exists(self, keywords):
        return self.neurons.has_key(keywords)

    def execute(self, keywords, args=None):
        return self.get(keywords)(args) if self.is_exists(keywords) else None
