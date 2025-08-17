import argparse
import os

from base_cli import BaseCli
from device.device import Device
from device.device_parameter import DeviceParameter


class DeviceCli(BaseCli):
    def __init__(self):
        super().__init__()
        self.device = Device()
        self.param_class = DeviceParameter
        self.category = self.device.category

    def register(self, subparsers):
        parser = subparsers.add_parser(
            self.category,
            help="Device related commands"
        )
        self.cmd_sp = parser.add_subparsers(dest=self.cmd_dest)

        # add common
        common_parser = argparse.ArgumentParser(add_help=False)
        self._add_common_args(common_parser)

        # register cmd
        self._register_dump_cmd(common_parser)

        parser.set_defaults(func=lambda args: parser.print_help())

    # -----------------------
    # Dump command
    # -----------------------
    def _register_dump_cmd(self, common_parser):
        sp = self.cmd_sp.add_parser(
            "dump",
            help="Dump device parameters to YAML file",
            parents=[common_parser]
        )
        sp.add_argument(
            "--output",
            help="Output YAML file path"
        )
        sp.set_defaults(func=self.dump)

    def dump(self, args):
        req_param = ["output"]
        if not self._is_exist_args(args, req_param):
            return

        param = DeviceParameter()
        param.update_parameter()
        filepath = os.path.join(self.device.device_data_dir, args.output)
        self._dump_param_to_file(param, filepath)
