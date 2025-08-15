from device.device import Device


class DeviceCli:
    def __init__(self):
        self.device = Device()

    def register(self, subparsers):
        parser = subparsers.add_parser(
            "device",
            help="Device related commands"
        )
        cmd_sp = parser.add_subparsers(dest="command")

        # tmp function
        sp_tmp = cmd_sp.add_parser(
            "tmp",
            help="Temporary command for testing"
        )
        sp_tmp.set_defaults(func=self._tmp_func)

        parser.set_defaults(func=lambda: parser.print_help())

    def _tmp_func(self):
        print("This is a temporary function in DeviceCli")
