import os
from dacite import from_dict
from lib.yaml_util import load_yaml, dump_yaml
from device.device_parameter import DeviceParameter


class Device:
    def __init__(self):
        self.param: DeviceParameter = None

    def set_parameter(self, param: DeviceParameter):
        self.param = param
