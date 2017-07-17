import unittest
from datetime import datetime

import cerebro.neurons.datetime_util as dt


class TestDatetime(unittest.TestCase):

    def setUp(self):
        self.response = datetime.now().strftime("%d-%m-%Y %H:%M")
        self.keyword = ("time", "date", "day")
        self.valid_attr = "KEYWORDS"

    def test_valid(self):
        assert hasattr(dt, self.valid_attr)

    def test_simple(self):
        assert dt.current_time() == self.response

    def test_neuron(self):
        assert dt.KEYWORDS[self.keyword]() == self.response
