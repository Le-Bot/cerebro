import unittest

import cerebro.core.entities as en


class TestEntities(unittest.TestCase):

    def setUp(self):
        self.keywords = ("book", "find")

    def test_command_creation(self):
        command = en.Command(self.keywords)
        assert len(command.keywords) == len(self.keywords)
