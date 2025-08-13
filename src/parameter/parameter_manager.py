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

    def dump_parameter(self, category):
        if not category:
            return

        self.parameters[category].dump_parameter()
