import config as cfg


class NLP(object):
    def __init__(self, parser, classifier):
        self.parser = parser
        self.clf = classifier
        self.ds = ()

    def parse_data_set(self):
        self.parser.parse()
        x = self.parser.get_column_data(cfg.COLUMN_FEATURE)
        y = self.parser.get_column_data(cfg.COLUMN_LABEL)
        self.ds = x, y

    def train(self):
        self.clf.fit(self.ds)

    def predict(self, x):
        return self.clf.predict(x)


