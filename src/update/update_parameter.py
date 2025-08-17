from parameter.base_parameter import BaseParameter
from dataclasses import dataclass


@dataclass
class UpdateParameter(BaseParameter):
    server: str = None
    filename: str = None
    url: str = None
