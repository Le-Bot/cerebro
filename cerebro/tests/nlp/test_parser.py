import unittest

import cerebro.nlp as n


class TestParser(unittest.TestCase):

    def setUp(self):
        self.obj = n.DataSetParser(n.DATA_SET_PATH)
        self.obj.parse()

    def test_parse(self):
        self.assertIsNotNone(self.obj.path)
        self.assertIsNotNone(self.obj.df)

    def test_column_data(self):
        temp = self.obj.get_column_data(n.COLUMN_LABEL)
        self.assertEqual(len(temp), 29)
