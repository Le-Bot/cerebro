import unittest

import cerebro.core.entities as en


class TestEntities(unittest.TestCase):

    def test_command_creation(self):
        command = en.Command(())