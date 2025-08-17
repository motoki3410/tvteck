from typing import Optional
from dataclasses import dataclass, field

from parameter.base_parameter import BaseParameter
from controller.livetv_kpi.livetv_kpi_parameter import LiveTvKpiParameter

controller_map = {
    "livetv_kpi": LiveTvKpiParameter
}


@dataclass
class ControllerParameter(BaseParameter):
    type: str = "default"
    type_param: Optional[BaseParameter] = None

    def set_type_param(self):
        self.type_param = controller_map.get(self.type)()
