import core.factory as default
from neuron.entities import Command

factory = default.DefaultFactory()
nlp, neuron = factory.cerebro()


def run(txt):
    label = nlp.predict(txt)
    return neuron.process(Command(label[0]))