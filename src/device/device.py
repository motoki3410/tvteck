from device.device_parameter import DeviceParameter


class Device:
    def __init__(self, device_param: DeviceParameter = None):
        self.param: DeviceParameter = device_param

    def set_parameter(self, param: DeviceParameter):
        self.param = param
