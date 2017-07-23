import sys

import cerebro.core.entities as en
import cerebro.core.usecases as uc
import cerebro.core.services as ser
import cerebro.core.constants as const


def init():
    config = ser.ConfigService()
    config.add_neurons_location(const.STR_DEFAULT_NEURONS_PATH)

    finder = ser.NeuronsFinderService()

    manager = ser.NeuronsService()
    cerebro = uc.CerebroMain(config, finder, manager)
    cerebro.load_all_neurons()

    return cerebro


def run(args):

    print("Initializing Cerebro ")
    cerebro = init()
    neurons = cerebro.manager.get_all()
    print("Cerebro initialized with % neurons".format(len(neurons)))

    print("Retrieving list of supported commands")
    print(neurons)
    for n in neurons.iterkeys():
        print(n)

    print("All system configured successfully.")

    print("Initializing command")
    command = en.Command(args)
    print("Command initialized")

    print("Executing command")
    print("Command Executed with following result:")
    print(cerebro.process_command(command))


print('Argument List:', str(sys.argv[1:]))
print("Running...")
run(tuple(sys.argv[1:]))

