import argparse

from base_cli import BaseCli
from test_manager.test_manager import TestManager
from test_manager.test_manager_parameter import TestManagerParameter


class TestManagerCli(BaseCli):
    def __init__(self):
        super().__init__()
        self.test_manager = TestManager()
        self.param_class = TestManagerParameter
        self.category = self.test_manager.category

    def register(self, subparsers):
        parser = subparsers.add_parser(
            self.category,
            help="Test Manager related commands"
        )
        self.cmd_sp = parser.add_subparsers(dest=self.cmd_dest)

        # add common
        common_parser = argparse.ArgumentParser(add_help=False)
        self._add_common_args(common_parser)

        # register cmd

        parser.set_defaults(func=lambda args: parser.print_help())
