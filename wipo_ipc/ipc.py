from .description import query_description, ipc_description_lookup
from .tools import convert_to_human, get_pure_group
from collections import namedtuple


ipc_part = namedtuple("ipc_part", "code description")


def gen_ipc_part(code):
    return ipc_part(code, query_description(code))


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

    def __repr__(self):
        return self.code

    def __eq__(self, value):
        return self.code == value

    def get_section(self):
        code = self.code[0]
        return gen_ipc_part(code)

    def get_classe(self):
        if len(self.code) >= 3:
            code = self.code[0:3]
            return gen_ipc_part(code)
        else:
            return None

    def get_subclass(self):
        if len(self.code) >= 4:
            code = self.code[0:4]
            return gen_ipc_part(code)
        else:
            return None

    def get_group(self):
        if len(self.code) == 14:
            code = get_pure_group(self.code)
            return gen_ipc_part(code)
        else:
            return None

    def get_subgroup(self):
        if len(self.code) == 14 and self.code[-6:] != "000000":
            code = self.code
            return gen_ipc_part(code)
        else:
            return None
