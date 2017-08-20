import neuron as neu
import nlp as n


def init_neuron():
    neu.cfg.add_neurons_location(neu.STR_DEFAULT_NEURONS_PATH)

    finder = neu.find

    manager = neu.NeuronsManager()
    return neu.Neuron(neu.cfg, finder, manager)


def init_nlp():
    parser = n.DataSetParser(n.DATA_SET_PATH)
    classifier = n.CerebroClassifier()
    return n.NLP(parser, classifier)


def init():
    neuron = init_neuron()
    neuron.load_all_neurons()

    nlp = init_nlp()
    nlp.parse_data_set()
    nlp.train()
