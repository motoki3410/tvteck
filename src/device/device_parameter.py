from parameter.base_parameter import BaseParameter
from dataclasses import dataclass


@dataclass
class DeviceConfig(BaseParameter):
    test: str = "test"


@dataclass
class DeviceParameter(BaseParameter):
    dsn: str = "jp_device_1"
    project: str = "wyoming"
    region: str = "jp"
    config: DeviceConfig = None
