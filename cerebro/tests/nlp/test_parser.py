import unittest

from cerebro.nlp.parser import DataSetParser
from cerebro.nlp.config import DATA_SET_PATH,COLUMN_LABEL


class TestParser(unittest.TestCase):

    def setUp(self):
        self.obj = DataSetParser(DATA_SET_PATH)
        self.obj.parse()

    def test_parse(self):
        assert self.obj.path is not None
        assert self.obj.df is not None

    def test_column_data(self):
        temp = self.obj.get_column_data(COLUMN_LABEL)
        assert len(temp) == 29
