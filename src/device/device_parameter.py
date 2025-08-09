from parameter.base_parameter import BaseParameter
from dataclasses import dataclass


@dataclass
class DeviceParameter(BaseParameter):
    device_type: str = "generic"
