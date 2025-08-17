from update.update_parameter import UpdateParameter


class Update:
    def __init__(self):
        self.param: UpdateParameter = None

    def set_parameter(self, param: UpdateParameter):
        self.param = param

    def download_fw(self):
        print("Downloading firmware...")
        print(self.param)
