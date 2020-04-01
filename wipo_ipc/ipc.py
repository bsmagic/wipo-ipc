from .description import Description, query_description, ipc_description_lookup
from .tools import convert_to_human, get_pure_group


class Ipc:
    """
    Main class that represents a IPC code
    """

    def __init__(self, code):
        if code not in ipc_description_lookup:
            raise ValueError

        self.code = code
        self.human_code = convert_to_human(self.code)
        self.section = self.get_section()
        self.classe = self.get_classe()
        self.subclass = self.get_subclass()
        self.group = self.get_group()
        self.subgroup = self.get_subgroup()
        self.description = self.get_descriptions()

    def __repr__(self):
        return self.code

    def __eq__(self, value):
        return self.code == value

    def get_section(self):
        return self.code[0]

    def get_classe(self):
        if len(self.code) >= 3:
            return self.code[0:3]
        else:
            return None

    def get_subclass(self):
        if len(self.code) >= 4:
            return self.code[0:4]
        else:
            return None

    def get_group(self):
        if len(self.code) == 14:
            return get_pure_group(self.code)
        else:
            return None

    def get_subgroup(self):
        if len(self.code) == 14 and self.code[-6:] != "000000":
            return self.code
        else:
            return None

    def get_descriptions(self):
        section = query_description(self.section)
        classe = query_description(self.classe)
        subclass = query_description(self.subclass)
        group = query_description(self.group)
        subgroup = query_description(self.subgroup)

        return Description(section, classe, subclass, group, subgroup)
