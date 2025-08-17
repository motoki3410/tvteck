import argparse

from base_cli import BaseCli
from update.update_parameter import UpdateParameter
from update.update import Update


class UpdateCli(BaseCli):
    def __init__(self):
        super().__init__()
        self.category = "update"
        self.update = Update()
        self.param_class = UpdateParameter

    def register(self, subparsers):
        parser = subparsers.add_parser(
            self.category,
            help="Update related commands"
        )
        self.cmd_sp = parser.add_subparsers(dest="command")

        # add common
        common_parser = argparse.ArgumentParser(add_help=False)
        self._add_common_args(common_parser)

        # register cmd
        self._register_download_cmd(common_parser)

        parser.set_defaults(func=lambda args: parser.print_help())

    # -------------------------
    # Download Command
    # -------------------------

    def _register_download_cmd(self, common_parser):
        sp = self.cmd_sp.add_parser(
            "download",
            help="Download firmware update",
            parents=[common_parser]
        )
        sp.add_argument(
            "--server",
            help="Firmware download server"
        )
        sp.add_argument(
            "--url",
            help="Firmware download URL"
        )
        sp.set_defaults(func=self.download)

    def download(self, args):
        req_param = ["server", "url"]
        param = self._resolve_parameter(args, req_param)
        if not param:
            return

        self.update.set_parameter(param)
        self.update.download_fw()
