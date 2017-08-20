import sys

import cerebro.neuron as neu


def init():
    neu.cfg.add_neurons_location(neu.STR_DEFAULT_NEURONS_PATH)

    finder = neu.find

    manager = neu.NeuronsManager()
    cerebro = neu.Neuron(neu.cfg, finder, manager)
    cerebro.load_all_neurons()

    return cerebro


def run(args):

    print("Initializing Cerebro ")
    cerebro = init()
    neurons = cerebro.manager.get_all()
    print("Cerebro initialized with {} neurons".format(len(neurons)))

    print("All system configured successfully.")

    command = neu.Command(args)

    print("Command Executed with following result:")
    print(cerebro.process_command(command))


print('Argument List: {}'.format(str(sys.argv[1:])))
print("Running...")
run(sys.argv[1:][0])


