import unittest

import cerebro.core.entities as en


class TestEntities(unittest.TestCase):

    def setUp(self):
        self.keyword = "book"
        self.test_keyword = "book"
        self.args = ("arg2", "arg1")
        self.test_args = ("arg2", "arg1")

    def test_command_creation(self):
        command = en.Command(self.keyword)
        assert command.keyword == self.test_keyword

    def test_command_creation_args(self):
        command = en.Command(self.keyword, self.args)
        assert command.keyword == self.test_keyword
        assert command.args == self.test_args
