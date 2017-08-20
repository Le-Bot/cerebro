import unittest
from datetime import datetime

import cerebro.neurons.datetime_util as dt


class TestDatetime(unittest.TestCase):

    def setUp(self):
        self.time_response = datetime.now().strftime("%H:%M")
        self.time_keyword = "time"
        self.date_response = datetime.now().strftime("%d-%m-%Y")
        self.date_keyword = "date"
        self.valid_attr = "KEYWORDS"

    def test_valid(self):
        assert hasattr(dt, self.valid_attr)

    def test_time(self):
        assert dt.current_time() == self.time_response

    def test_neuron_time(self):
        assert dt.KEYWORDS[self.time_keyword]() == self.time_response

    def test_date(self):
        assert dt.current_date() == self.date_response

    def test_neuron_date(self):
        assert dt.KEYWORDS[self.date_keyword]() == self.date_response
