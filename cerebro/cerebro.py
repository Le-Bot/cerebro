from core import usecases as uc, services as ser, constants as const, config as cfg
import nlp as n


def init_neuron():
    cfg.add_neurons_location(const.STR_DEFAULT_NEURONS_PATH)

    finder = ser.find_neurons

    manager = ser.NeuronsService()
    return uc.CerebroMain(cfg, finder, manager)


def init_nlp():
    parser = n.DataSetParser(n.DATA_SET_PATH)
    classifier = n.CerebroClassifier()
    return n.NLP(parser, classifier)


def init():
    cerebro = init_neuron()
    cerebro.load_all_neurons()

    nlp = init_nlp()
    nlp.parse_data_set()
    nlp.train()
