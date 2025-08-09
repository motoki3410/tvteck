from device.device_parameter import DeviceParameter
from update.update_paramter import UpdateParameter

param_map = {
    "device": DeviceParameter,
    "update": UpdateParameter,
}


class ParameterManager():
    def __init__(self):
        self.parameters = {}

    def add_parameter(self, name: str, param):
        self.parameters[name] = param

    def add_all_parameters(self):
        for name, param_class in param_map.items():
            self.parameters[name] = param_class()

    def show_parameters(self, all: bool = False):
        self.add_all_parameters()

        for name, param in self.parameters.items():
            param.show_parameters()
