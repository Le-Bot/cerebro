import constants as const


class CerebroMain(object):
    def __init__(self, config, finder, manager):
        self.config = config
        self.finder = finder
        self.manager = manager

    def load_all_neurons(self):
        path = self.config.get_neurons_path()
        neuron_modules = self.finder.find_neurons(path)
        for neuron in neuron_modules:
            if self.manager.is_valid(neuron):
                self.manager.add(neuron.KEYWORDS)

    def process_command(self, command):
        response = self.manager.execute(command.keywords, command.args)
        return response if response is not None else const.STR_DEFAULT_RESPONSE
