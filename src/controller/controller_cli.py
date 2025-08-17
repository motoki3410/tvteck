import argparse
import os

from base_cli import BaseCli
from controller.controller import Controller
from controller.controller_parameter import ControllerParameter


class ControllerCli(BaseCli):
    def __init__(self):
        super().__init__()
        self.controller = Controller()
        self.param_class = ControllerParameter
        self.category = self.controller.category

    def register(self, subparsers):
        parser = subparsers.add_parser(
            self.category,
            help="Controller related commands"
        )
        self.cmd_sp = parser.add_subparsers(dest=self.cmd_dest)

        # add common
        common_parser = argparse.ArgumentParser(add_help=False)
        self._add_common_args(common_parser)

        # register cmd

        parser.set_defaults(func=lambda args: parser.print_help())
