from typing import Optional
from dataclasses import dataclass

from parameter.base_parameter import BaseParameter


@dataclass
class LiveTvKpiParameter(BaseParameter):
    kpi: Optional[str] = "channel_switch"
    repeat_num: Optional[int] = 0
