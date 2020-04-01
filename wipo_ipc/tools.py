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
    output = ""
    output += ipc_code[0:4]
    output += ' '
    i = 4
    for char in ipc_code[4:8]:
        if char != '0':
            output += ipc_code[i:8]
            break
        i += 1
    output += '/'
    if ipc_code[8] == '0':
        output += ipc_code[8:10]
    else:
        i = 8
        for char in ipc_code[8:]:
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