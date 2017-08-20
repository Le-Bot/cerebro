import sys

import cerebro.neuron.entities as en
import cerebro.neuron.neuron as uc
import cerebro.neuron.manager as ser
import cerebro.neuron.constants as const
import cerebro.neuron.config as cfg
import cerebro.neuron.finder as fn


def init():
    cfg.add_neurons_location(const.STR_DEFAULT_NEURONS_PATH)

    finder = fn.find

    manager = ser.NeuronsManager()
    cerebro = uc.Neuron(cfg, finder, manager)
    cerebro.load_all_neurons()

    return cerebro


def run(args):

    print("Initializing Cerebro ")
    cerebro = init()
    neurons = cerebro.manager.get_all()
    print("Cerebro initialized with {} neurons".format(len(neurons)))

    print("All system configured successfully.")

    command = en.Command(args)

    print("Command Executed with following result:")
    print(cerebro.process_command(command))


print('Argument List: {}'.format(str(sys.argv[1:])))
print("Running...")
run(sys.argv[1:][0])


