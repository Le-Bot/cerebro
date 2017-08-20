import sys

import cerebro.cerebro as cer


def run(args):
    print(cer.run(args))

run(sys.argv[1:])


