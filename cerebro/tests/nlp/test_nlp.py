import unittest
import numpy as np

import cerebro.nlp as n


class TestNLP(unittest.TestCase):

    def setUp(self):
        parser = n.DataSetParser(n.DATA_SET_PATH)
        classifier = n.CerebroClassifier()
        self.obj = n.NLP(parser, classifier)
    
    def test_init(self):
        self.assertIsNotNone(self.obj.parser)
        self.assertIsNotNone(self.obj.clf)
        self.assertIsNone(self.obj.x)
        self.assertIsNone(self.obj.y)
    
    def test_parse_data_set(self):
        self.obj.parse_data_set()
        self.assertEqual(len(self.obj.x), 29)
        self.assertEqual(len(self.obj.y), 29)

    def test_train(self):
        self.obj.parse_data_set()
        self.obj.train()

    def test_predict(self):
        self.obj.parse_data_set()
        self.obj.train()
        test_y = self.obj.predict(["How are you"])
        self.assertGreater(np.mean(test_y == ["greet"]), 0.5)
