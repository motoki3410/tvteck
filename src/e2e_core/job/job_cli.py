import argparse

from base_cli import BaseCli
from e2e_core.job.job import Job


class JobCli(BaseCli):
    def __init__(self):
        super().__init__()
        self.job = Job()
        self.category = self.job.category

    def register(self, subparsers):
        parser = subparsers.add_parser(
            self.category,
            help="Job-related commands"
        )
        self.cmd_sp = parser.add_subparsers(dest=self.cmd_dest)

        # add common
        common_parser = argparse.ArgumentParser(add_help=False)
        self._add_common_args(common_parser)

        # register cmd
        self._register_create_cmd()

        parser.set_defaults(func=lambda args: parser.print_help())

    # ---------------------
    # Create new job file
    # ---------------------
    def _register_create_cmd(self):
        sp = self.cmd_sp.add_parser(
            "create",
            help="Create a new job file"
        )
        sp.add_argument(
            "--name",
            type=str,
            help="Name of the job"
        )
        sp.set_defaults(func=self.create)

    def create(self, args):
        req_param = ["name"]
        if not self._is_exist_args(args, req_param):
            return

        self.job.create_new_job_file(args.name)
