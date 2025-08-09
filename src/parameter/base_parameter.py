from dataclasses import dataclass, fields


@dataclass
class BaseParameter:
    def show_parameters(self):
        fields_list = [f.name for f in fields(self)]
        print(fields_list)
