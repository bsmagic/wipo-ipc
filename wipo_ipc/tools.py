def convert_to_human(ipc_code: str) -> str:
    """
    Args:
        ipc_code: string representation of a IPC code in official form

    Returns:
        str: string representation of the input IPC code in human-friendly form

    Example:
        >>> convert_to_human("A61F0005580000")
        "A61F 5/58"
    """
    if len(ipc_code) <= 4:
        return ipc_code

    output = ipc_code[0:4] + ' '

    group = ipc_code[4:8]
    for i, char in enumerate(group):
        if char != '0':
            output += group[i:] + '/'
            break

    subgroup = ipc_code[8:]
    # if subgroup started with zero -> subgroup is 0X where 0<=X<=9
    if subgroup[0] == '0':
        output += subgroup[0:2]
    else:
        for i, char in enumerate(subgroup):
            if char != '0':
                output += char
            else:
                if i == 1:
                    output += char
                    return output
                else:
                    return output
    return output


def convert_to_official(ipc: str) -> str:
    """
    Args:
        ipc_code: string representation of a IPC code in human-friendly form

    Returns:
        str: string representation of the input IPC code in official form

    Example:

        >>> convert_to_official("A61F 5/58")
        "A61F0005580000"
    """

    if len(ipc) <= 4:
        return ipc

    ready, to_process = ipc.split()
    group, subgroup = to_process.split("/")

    str_group = ""
    str_group += "0" * (4-len(group))
    str_group += group

    str_subgroup = ""
    str_subgroup += subgroup
    str_subgroup += "0" * (6 - len(subgroup))

    return ready + str_group + str_subgroup


def get_pure_group(ipc_code: str) -> str:
    """
    Args:
        ipc_code: string representation of a full IPC code


    Returns:
        str: string representation of the group of the input ipc code

    Example:
        >>> get_pure_group("A61F0005580000")
        A61F0005000000
    """
    return ipc_code[0:8] + '000000'
