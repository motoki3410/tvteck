from datetime import datetime

from parameter.base_parameter import BaseParameter
from dataclasses import dataclass


@dataclass
class JobParameter(BaseParameter):
    name: str = None
    created: str = None

    def set_new_job_info(self, name):
        self.name = name
        self.created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
