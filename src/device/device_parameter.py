from parameter.base_parameter import BaseParameter
from dataclasses import dataclass, field


@dataclass
class DeviceConfig(BaseParameter):
    test: str = None
    update: bool = False


@dataclass
class DeviceParameter(BaseParameter):
    dsn: str = None
    project: str = None
    region: str = None
    config: DeviceConfig = field(default_factory=DeviceConfig)

    def update_parameter(self):
        self.project = "updated_project"
        self.region = "updated_region"
        self.config = DeviceConfig()
