import csv
import os

ipc_path = os.path.join(os.path.dirname(__file__), "data/all_ipc.csv")

with open(ipc_path, "r") as file_data:
    reader = csv.reader(file_data, dialect='excel-tab')
    ipc_description_lookup = {}
    for row in reader:
        try:
            ipc_description_lookup[row[0]] = row[1]
        except IndexError:
            continue


def get_pure_group(ipc):
    return ipc[0:8] + '000000'


def query_description(ipc):
    return ipc_description_lookup[ipc]


def convert_to_human(ipc):
    """
    ex: A63B0055000000 --> A63B 55/00
        A61F0005580000 --> A61F 5/58
    """
    if len(ipc) <= 4:
        return ipc
    output = ""
    output += ipc[0:4]
    output += ' '
    i = 4
    for char in ipc[4:8]:
        if char != '0':
            output += ipc[i:8]
            break
        i += 1
    output += '/'
    if ipc[8] == '0':
        output += ipc[8:10]
    else:
        i = 8
        for char in ipc[8:]:
            if char != '0':
                output += char
            else:
                if i == 9:
                    output += char
                    break
                else:
                    break
            i += 1
    return output


def convert_to_official(ipc):
    """
    ex: A63B 55/00 --> A63B0055000000
        A61F 5/58 --> A61F0005580000
    """

    if len(ipc) <= 4:
        return ipc

    ready, to_process = ipc.split()
    group, subgroup = to_process.split("/")

    str_group = ""
    for i in range(4 - len(group)):
        str_group += "0"
    str_group += group

    str_subgroup = ""
    str_subgroup += subgroup
    for i in range(6 - len(subgroup)):
        str_subgroup += "0"

    return ready + str_group + str_subgroup


class Description:
    def __init__(self, section, classe, subclass, group, subgroup):
        self.section = section
        self.classe = classe
        self.subclass = subclass
        self.group = group
        self.subgroup = subgroup


class Ipc:
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
