import sys

import cerebro.core.entities as en
import cerebro.core.usecases as uc
import cerebro.core.manager as ser
import cerebro.core.constants as const
import cerebro.core.config as cfg
import cerebro.core.finder as fn


def init():
    cfg.add_neurons_location(const.STR_DEFAULT_NEURONS_PATH)

    finder = fn.find

    manager = ser.NeuronsService()
    cerebro = uc.CerebroMain(cfg, finder, manager)
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


