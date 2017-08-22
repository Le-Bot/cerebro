import core.factory as default
from neuron.entities import Command


def run(txt, factory=None):

    if factory is None:
        factory = default.DefaultFactory()

    nlp, neuron = factory.cerebro()
    label = nlp.predict(txt)
    return neuron.process(Command(label[0]))