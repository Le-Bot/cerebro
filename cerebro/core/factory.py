import abc

import cerebro.neuron as neu
import cerebro.nlp as n


class BaseFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def neuron(self):
        return

    @abc.abstractmethod
    def nlp(self):
        return

    def cerebro(self):
        neuron = self.neuron()
        neuron.load_all()

        nlp = self.nlp()
        nlp.parse_data_set()
        nlp.train()

        return nlp, neuron


class DefaultFactory(BaseFactory):

    def neuron(self):
        neu.cfg.add_neurons_location(neu.STR_DEFAULT_NEURONS_PATH)
        finder = neu.find
        manager = neu.NeuronsManager()
        return neu.Neuron(neu.cfg, finder, manager)

    def nlp(self):
        parser = n.DataSetParser(n.DATA_SET_PATH)
        classifier = n.CerebroClassifier()
        return n.NLP(parser, classifier)
