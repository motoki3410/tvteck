from typing import Optional

from parameter.base_parameter import BaseParameter
from dataclasses import dataclass


@dataclass
class TestManagerParameter(BaseParameter):
    name: str = "default"
