from typing import Optional

from parameter.base_parameter import BaseParameter
from dataclasses import dataclass, field


@dataclass
class DeviceConfig(BaseParameter):
    test: Optional[str] = None
    update: bool = False


@dataclass
class DeviceParameter(BaseParameter):
    dsn: Optional[str] = None
    project: Optional[str] = None
    region: Optional[str] = None
    config: DeviceConfig = field(default_factory=DeviceConfig)

    def update_parameter(self):
        self.project = "updated_project"
        self.region = "updated_region"
        self.config = DeviceConfig()
