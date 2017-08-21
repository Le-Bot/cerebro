import unittest
import numpy as np

from cerebro.nlp.classifier import CerebroClassifier, AbstractClassifier


class TestClassifier(unittest.TestCase):

    def setUp(self):
        self.obj = CerebroClassifier()
        self.test_x = ["test1", "test2"]
        self.test_y = ["t1", "t2"]

    def test_type(self):
        assert isinstance(self.obj, AbstractClassifier)

    def test_init(self):
        assert self.obj.clf is not None

    def test_fit(self):
        self.obj.fit(self.test_x, self.test_y)
        assert np.mean(self.obj.predict(self.test_x) == self.test_y) > 0.5


