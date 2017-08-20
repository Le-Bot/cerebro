from core import usecases as uc, manager as ser, constants as const, config as cfg, finder as fn
import nlp as n


def init_neuron():
    cfg.add_neurons_location(const.STR_DEFAULT_NEURONS_PATH)

    finder = fn.find

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
