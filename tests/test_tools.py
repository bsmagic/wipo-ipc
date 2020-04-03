from wipo_ipc import tools

complete_human = "A23B 9/32"
complete_official = "A23B0009320000"

subgroup_X0_official = "C05B0011100000"
subgroup_X0_human = "C05B 11/10"

group_only_official = "A23B0009000000"
group_only_human = "A23B 9/00"

subclass_only = "A23B"


def test_convert_to_human():
    assert tools.convert_to_human(complete_official) == complete_human
    assert tools.convert_to_human(subgroup_X0_official) == subgroup_X0_human
    assert tools.convert_to_human(subclass_only) == subclass_only
    assert tools.convert_to_human(group_only_official) == group_only_human


def test_convert_to_official():
    assert tools.convert_to_official(complete_human) == complete_official
    assert tools.convert_to_official(subclass_only) == subclass_only


def test_get_puregroup():
    assert tools.get_pure_group(complete_official) == "A23B0009000000"
