import unittest

import cerebro.nlp as n


class TestParser(unittest.TestCase):

    def setUp(self):
        self.obj = n.DataSetParser(n.DATA_SET_PATH)
        self.obj.parse()

    def test_parse(self):
        assert self.obj.path is not None
        assert self.obj.df is not None

    def test_column_data(self):
        temp = self.obj.get_column_data(n.COLUMN_LABEL)
        assert len(temp) == 29
