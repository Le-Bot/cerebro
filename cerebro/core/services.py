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

    def get_all_neurons(self):
        return self.neurons

    def add_neuron(self, obj):
        self.neurons.update(obj)

    @staticmethod
    def is_valid_neuron(neuron):
        return hasattr(neuron, const.STR_KEYWORDS)

    def get_neuron(self, keywords):
        return self.neurons.get(keywords, None)

    def is_exists_neuron(self, keywords):
        return self.neurons.has_key(keywords)

    def execute_neuron(self, keywords, args=None):
        return self.get_neuron(keywords)(args) if self.is_exists_neuron(keywords) else None
