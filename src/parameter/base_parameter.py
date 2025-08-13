from dataclasses import dataclass, fields, is_dataclass, asdict


@dataclass
class BaseParameter:
    def get_field_names(self):
        field_names = []
        for field in fields(self):
            if is_dataclass(field.type):
                field_names.extend(self.get_field_names(field.type))
            else:
                field_names.append(field.name)

        return field_names

    def dump_parameter(self):
        print(asdict(self))
