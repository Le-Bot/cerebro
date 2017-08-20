import config as cfg


class NLP(object):
    def __init__(self, parser, classifier):
        self.parser = parser
        self.clf = classifier
        self.x, self.y = None, None

    def parse_data_set(self):
        self.parser.parse()
        self.x = self.parser.get_column_data(cfg.COLUMN_FEATURE)
        self.y = self.parser.get_column_data(cfg.COLUMN_LABEL)

    def train(self):
        self.clf.fit(self.x, self.y)

    def predict(self, x):
        return self.clf.predict(x)


