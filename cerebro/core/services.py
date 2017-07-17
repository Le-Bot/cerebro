class ConfigService(object):
    def __init__(self):
        self.__neurons_path = []

    def add_neurons_location(self, path):
        self.__neurons_path.append(path)

    def get_neurons_path(self):
        return self.__neurons_path