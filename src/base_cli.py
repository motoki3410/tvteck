from abc import ABC, abstractmethod

from parameter.parameter_manager import ParameterManager


class BaseCli(ABC):
    def __init__(self):
        self.category = None
        self.cmd_sp = None
        self.param_class = None

    @abstractmethod
    def register(self, subparsers):
        pass

    def _add_common_args(self, parser):
        parser.add_argument(
            "--param",
            help="Use parameter from parameter manager"
        )

    def _show_command_help(self, args, msg):
        if msg:
            print(msg)
        self.cmd_sp.choices.get(args.command).print_help()

    def _load_param(self, filepath):
        pm = ParameterManager()
        pm.load_parameter_file(filepath)

        return pm.get_parameter(self.category)

    def _is_exist_args(self, args, req_args):
        missing = [name for name in req_args if not getattr(args, name, None)]
        if missing:
            self._show_command_help(
                args,
                f"Missing arguments for {args.command}: {', '.join(missing)}"
            )
            return False
        else:
            return True

    def _resolve_parameter(self, args, req_args):
        if getattr(args, "param", None):
            return self._load_param(args.param)

        if not self._is_exist_args(args, req_args):
            return None

        param = self.param_class()
        for name in req_args:
            setattr(param, name, getattr(args, name, None))

        return param
