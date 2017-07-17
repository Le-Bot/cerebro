

import constants as const

NEURONS = {}


def get_all_neurons(path):
    pass


def process_command(command):
    response = const.STR_DEFAULT_RESPONSE
    for key, value in NEURONS.iteritems():
        if command.keywords == key:
            response = value(command.args)
            break

    return response

