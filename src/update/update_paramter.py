from parameter.base_parameter import BaseParameter
from dataclasses import dataclass


@dataclass
class UpdateParameter(BaseParameter):
    update_frequency: int = 24
