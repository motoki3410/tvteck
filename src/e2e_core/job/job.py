import os
from datetime import datetime

from lib.yaml_util import dump_yaml
from parameter.parameter_manager import ParameterManager


class Job:
    def __init__(self):
        self.job_data_dir = "data/job"

    def create_new_job_file(self, job_name):
        filename = f"{job_name}.yaml"
        filepath = os.path.join(self.job_data_dir, filename)

        pm = ParameterManager()
        pm.set_all_parameters()

        job_categories = list(pm.param_map.keys())
        job_categories.remove("device")

        param_dict = {
            "name": job_name,
            "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        pm.create_param_dict(param_dict, job_categories)
        dump_yaml(param_dict, filepath)
