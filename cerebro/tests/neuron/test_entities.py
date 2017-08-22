import unittest

import cerebro.neuron.entities as en


class TestEntities(unittest.TestCase):

    def setUp(self):
        self.keyword = "book"
        self.test_keyword = "book"
        self.args = ("arg2", "arg1")
        self.test_args = ("arg2", "arg1")

    def test_command_creation(self):
        command = en.Command(self.keyword)
        self.assertEquals(command.keyword, self.test_keyword)

    def test_command_creation_args(self):
        command = en.Command(self.keyword, self.args)
        self.assertEquals(command.keyword, self.test_keyword)
        self.assertEquals(command.args, self.test_args)
