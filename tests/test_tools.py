from wipo_ipc import tools

ipc_human = "A23B 9/32"
ipc_official = "A23B0009320000"


def test_convert_to_human():
    assert tools.convert_to_human(ipc_official) == ipc_human


def test_convert_to_official():
    assert tools.convert_to_official(ipc_human) == ipc_official


def test_get_puregroup():
    assert tools.get_pure_group(ipc_official) == "A23B0009000000"
