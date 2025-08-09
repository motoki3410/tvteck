from device.device_parameter import DeviceParameter
from update.update_parameter import UpdateParameter

from dataclasses import fields

param_map = {
    "device": DeviceParameter,
    "update": UpdateParameter,
}


class ParameterManager():
    def __init__(self):
        self.parameters = {}

    def set_parameter(self, name: str, param):
        self.parameters[name] = param

    def set_all_parameters(self):
        for name, param_class in param_map.items():
            self.parameters[name] = param_class()

    def show_field_name(self):
        for name, param in param_map.items():
            field_names = [f.name for f in fields(param)]
            print(f"{name}: {field_names}")
