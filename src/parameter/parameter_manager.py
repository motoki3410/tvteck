import os

from dacite import from_dict
from lib.yaml_util import load_yaml, dump_yaml
from device.device_parameter import DeviceParameter
from update.update_parameter import UpdateParameter
from e2e_core.job.job_info import JobParameter


class ParameterManager():
    param_map = {
        "job_info": JobParameter,
        "device": DeviceParameter,
        "update": UpdateParameter,
    }

    def __init__(self):
        self.parameters = {}

    def set_parameter(self, name: str, param):
        """
        Set a parameter instance for a given category name.

        Args:
            name: Category name (e.g. 'device').
            param: Parameter instance (dataclass) to store.
        """
        self.parameters[name] = param

    def set_all_parameters(self):
        """
        Initialize all known parameter categories with default instances.
        """
        for name, param_class in self.param_map.items():
            self.parameters[name] = param_class()

    def get_parameter(self, name: str):
        """
        Retrieve a stored parameter instance by category name.

        Args:
            name: Category name (e.g. 'device').

        Returns:
            The parameter instance or None if not found.
        """
        return self.parameters.get(name)

    def get_field_names(self, category=None):
        """
        Return field names for the parameter dataclass of a category.

        Args:
            category: Category name whose field names to return.

        Returns:
            A list of field names, or None if category is not provided.
        """
        if not category:
            return

        param = self.param_map.get(category)
        return param.get_field_names(param)

    def get_all_category_field_names(self):
        """
        Return a dict mapping each category to its field name list.
        """
        params = {}
        for name, param in self.param_map.items():
            params[name] = param.get_field_names(param)
        return params

    def load_parameter_file(self, filename):
        """
        Load parameters from a YAML file and populate `self.parameters`.

        Args:
            filename: Path under the `data/` directory to load.
        """
        file_path = os.path.join("data/", filename)
        load_param = load_yaml(file_path)

        for name, params in load_param.items():
            param_class = self.param_map.get(name)
            if param_class:
                self.set_parameter(name, from_dict(param_class, params))

    def dump_parameter_file(self, filename, categories=None):
        """
        Dump current parameters to a YAML file under `data/`.

        Args:
            filename: Output filename under the `data/` directory.
        """
        filepath = os.path.join("data/", f"{filename}.yaml")
        param_dict = {}

        if not categories:
            categories = self.parameters.keys()

        for category in categories:
            param = self.get_parameter(category)
            if param:
                param_dict[category] = param.dump_parameter()

        dump_yaml(param_dict, filepath)

    def show_parameter(self):
        """
        Print stored parameters to stdout for quick inspection.
        """
        for name, param in self.parameters.items():
            print(f"Parameter Name: {name}")
            print(f"Parameter Value: {param}")
            print("-" * 20)
