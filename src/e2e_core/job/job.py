import os

from parameter.parameter_manager import ParameterManager
from e2e_core.job.job_info import JobParameter


class Job:
    def __init__(self):
        self.category = "job"
        self.job_data_dir = "job"
        self.param_name = "job_info"

    def create_new_job_file(self, job_name):
        filepath = os.path.join(self.job_data_dir, job_name)

        param = JobParameter()
        param.set_new_job_info(job_name)

        pm = ParameterManager()
        pm.set_all_parameters()

        job_categories = list(pm.param_map.keys())
        job_categories.remove("device")

        pm.set_parameter(self.param_name, param)
        pm.dump_parameter_file(filepath, job_categories)

    def load_job_file(self, job_name):
        filepath = os.path.join(self.job_data_dir, job_name)

        pm = ParameterManager()
        pm.load_parameter_file(filepath)
