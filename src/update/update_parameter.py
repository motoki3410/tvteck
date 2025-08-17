from typing import Optional

from parameter.base_parameter import BaseParameter
from dataclasses import dataclass


@dataclass
class UpdateParameter(BaseParameter):
    server: Optional[str] = None
    filename: Optional[str] = None
    url: Optional[str] = None
