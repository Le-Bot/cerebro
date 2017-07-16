import unittest

import cerebro.core.entities as en


class TestEntities(unittest.TestCase):

    def setUp(self):
        self.keywords = ("book", "find")
        self.test_keywords = ("book", "find")
        self.args = ("arg2", "arg1")
        self.test_args = ("arg2", "arg1")

    def test_command_creation(self):
        command = en.Command(self.keywords)
        assert command.keywords == self.test_keywords

    def test_command_creation_args(self):
        command = en.Command(self.keywords, self.args)
        assert command.keywords == self.test_keywords
        assert command.args == self.test_args
