from device.device_parameter import DeviceParameter


class Device:
    def __init__(self, device_param: DeviceParameter = DeviceParameter()):
        self.param: DeviceParameter = device_param

    def set_parameter(self, param: DeviceParameter):
        self.param = param

    def show_parameters(self):
        self.param.show_parameters()


def main():
    param = DeviceParameter()
    device = Device(param)
