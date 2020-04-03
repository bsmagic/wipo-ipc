import csv
import os
from collections import namedtuple

ipc_path = os.path.join(os.path.dirname(__file__), "data/all_ipc.csv")

with open(ipc_path, "r") as file_data:
    reader = csv.reader(file_data, dialect='excel-tab')
    ipc_description_lookup = {}
    for row in reader:
        try:
            ipc_description_lookup[row[0]] = row[1]
        except IndexError:
            continue

Description = namedtuple(
    'Description', 'section classe subclass group subgroup')


def query_description(ipc_code: str) -> str:
    """
    Args:
        ipc_code: string representation of a IPC code

    Returns:
        str: description of the IPC code

    Examples:
        >>> query_description("A")
        "HUMAN NECESSITIES"
        >>> query_description("A23B0009320000")
        "Apparatus for preserving using liquids"
    """
    return ipc_description_lookup[ipc_code]
