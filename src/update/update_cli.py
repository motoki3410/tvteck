import argparse
from update.update import Update


class UpdateCli:
    def __init__(self):
        self.update = Update()
        self.cmd_sp = None

    def register(self, subparsers):
        parser = subparsers.add_parser(
            "update",
            help="Update related commands"
        )
        self.cmd_sp = parser.add_subparsers(dest="command")

        # add common
        common_parser = argparse.ArgumentParser(add_help=False)
        self._add_common_args(common_parser)

        # register cmd
        self._register_download_cmd(common_parser)
        self._register_tmp_cmd(common_parser)

        parser.set_defaults(func=lambda args: parser.print_help())

    def _add_common_args(self, parser):
        parser.add_argument(
            "--param",
            help="Use parameter from parameter manager",
            action="store_true"
        )

    def _show_command_help(self, args, msg):
        if msg:
            print(msg)
        self.cmd_sp.choices.get(args.command).print_help()

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
        if args.param:
            print("Using parameter manager for download.")
            return
        else:
            req_args = ["server", "url"]
            missing = [name for name in req_args if not getattr(args, name, None)]
            if missing:
                self._show_command_help(
                    args,
                    f"Missing arguments for download: {', '.join(missing)}"
                )
                return

    # -------------------------
    # Tmp command
    # -------------------------

    def _register_tmp_cmd(self, common_parser):
        sp = self.cmd_sp.add_parser(
            "tmp",
            help="Temporary command for testing",
            parents=[common_parser]
        )
        sp.add_argument(
            "--dsn",
            help="Data Source Name"
        )
        sp.set_defaults(func=self.tmp)

    def tmp(self, args):
        if not args.dsn:
            self._show_command_help(args, "Missing arguments for tmp command.")
            return
        self.update.install_fw(args.dsn)
