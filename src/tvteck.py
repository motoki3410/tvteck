import argparse

from device.device_cli import DeviceCli
from update.update_cli import UpdateCli

category_map = {
    "device": DeviceCli,
    "update": UpdateCli
}


def main():
    parser = argparse.ArgumentParser(description="TVTeck Client Script")
    subparsers = parser.add_subparsers(dest="category")

    # set cli command for each category
    for _, cli_class in category_map.items():
        cli_instance = cli_class()
        cli_instance.register(subparsers)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
