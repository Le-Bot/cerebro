import unittest
import numpy as np

import cerebro.nlp as n


class TestNLP(unittest.TestCase):

    def setUp(self):
        parser = n.DataSetParser(n.DATA_SET_PATH)
        classifier = n.CerebroClassifier()
        self.obj = n.NLP(parser, classifier)
    
    def test_init(self):
        assert self.obj.parser is not None
        assert self.obj.clf is not None
        assert self.obj.x is None
        assert self.obj.y is None
    
    def test_parse_data_set(self):
        self.obj.parse_data_set()
        assert len(self.obj.x) == 29
        assert len(self.obj.y) == 29

    def test_train(self):
        self.obj.parse_data_set()
        self.obj.train()

    def test_predict(self):
        self.obj.parse_data_set()
        self.obj.train()
        test_y = self.obj.predict(["How are you"])
        assert np.mean(test_y == ["greet"]) > 0.5
    
    