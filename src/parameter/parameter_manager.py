import os

from dacite import from_dict
from lib.yaml_util import load_yaml, dump_yaml
from device.device_parameter import DeviceParameter
from update.update_parameter import UpdateParameter


class ParameterManager():
    param_map = {
        "device": DeviceParameter,
        "update": UpdateParameter,
    }

    def __init__(self):
        self.parameters = {}

    def set_parameter(self, name: str, param):
        self.parameters[name] = param

    def set_all_parameters(self):
        for name, param_class in self.param_map.items():
            self.parameters[name] = param_class()

    def get_parameter(self, name: str):
        return self.parameters.get(name)

    def get_field_names(self, category=None):
        if not category:
            return

        param = self.param_map.get(category)
        return param.get_field_names(param)

    def get_all_category_field_names(self):
        params = {}
        for name, param in self.param_map.items():
            params[name] = param.get_field_names(param)
        return params

    def load_parameter_file(self, filename):
        file_path = os.path.join("data/", filename)
        load_param = load_yaml(file_path)

        for name, params in load_param.items():
            param_class = self.param_map.get(name)
            if param_class:
                self.set_parameter(name, from_dict(param_class, params))

    def dump_parameter_file(self, filename):
        filepath = os.path.join("data/", filename)
        param_dict = {}
        for name, param in self.parameters.items():
            param_dict[name] = param.dump_parameter()
        dump_yaml(param_dict, filepath)

    def show_parameter(self):
        for name, param in self.parameters.items():
            print(f"Parameter Name: {name}")
            print(f"Parameter Value: {param}")
            print("-" * 20)
