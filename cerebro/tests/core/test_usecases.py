import unittest

import cerebro.core.entities as en
import cerebro.core.usecases as uc
import cerebro.core.services as ser
import cerebro.core.constants as const
import cerebro.core.config as cfg


class TestUseCases(unittest.TestCase):
    def setUp(self):
        cfg.add_neurons_location(const.STR_DEFAULT_NEURONS_PATH)

        self.finder = ser.find_neurons

        self.manager = ser.NeuronsService()

        self.command_args = ("arg1", "arg2")

    def test_cerebro_creation(self):
        cerebro = uc.CerebroMain(cfg, self.finder, self.manager)
        assert cerebro
        assert cerebro.config == cfg
        assert cerebro.finder == self.finder
        assert cerebro.manager == self.manager

    def test_load_all_neurons(self):
        cerebro = uc.CerebroMain(cfg, self.finder, self.manager)
        cerebro.load_all_neurons()
        assert len(self.manager.get_all()) > 0

    def test_command_execution(self):
        test_keyword = "system check"
        test_response = "All working properly."
        test_command = en.Command(test_keyword, self.command_args)

        cerebro = uc.CerebroMain(cfg, self.finder, self.manager)
        cerebro.load_all_neurons()

        response = cerebro.process_command(test_command)
        assert response == test_response

    def test_command_execution_failure(self):
        test_keyword = "wrong command"
        test_command = en.Command(test_keyword)

        cerebro = uc.CerebroMain(cfg, self.finder, self.manager)
        cerebro.load_all_neurons()

        response = cerebro.process_command(test_command)
        assert response == const.STR_DEFAULT_RESPONSE
