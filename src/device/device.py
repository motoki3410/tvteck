import os
from device.device_parameter import DeviceParameter


class Device:
    def __init__(self):
        self.category = "device"
        self.device_data_dir = "device"
        self.param: DeviceParameter = None

    def set_parameter(self, param: DeviceParameter):
        self.param = param
