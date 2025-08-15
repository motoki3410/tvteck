from update.update_parameter import UpdateParameter


class Update:
    def __init__(self):
        self.param: UpdateParameter = None

    def install_fw(self, dsn):
        print(f"Installing firmware for {dsn}")
