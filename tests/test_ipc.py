from wipo_ipc import ipc

ipc_human = "A23B 9/32"
ipc_official = "A23B0009320000"
instance = ipc.Ipc(ipc_official)


def test_convert_to_human():
    assert ipc.convert_to_human(ipc_official) == ipc_human


def test_convert_to_official():
    assert ipc.convert_to_official(ipc_human) == ipc_official


def test_get_puregroup():
    assert ipc.get_pure_group(ipc_official) == "A23B0009000000"


def test_partes():
    assert instance.section == "A"
    assert instance.classe == "A23"
    assert instance.subclass == "A23B"
    assert instance.group == "A23B0009000000"
    assert instance.subgroup == "A23B0009320000"


def test_query_description():
    funcao = ipc.query_description
    assert funcao(instance.section) == "HUMAN NECESSITIES"
    assert funcao(
        instance.classe) == "FOODS OR FOODSTUFFS; THEIR TREATMENT, NOT COVERED BY OTHER CLASSES"
    assert funcao(instance.subclass) == "PRESERVING, e.g. BY CANNING, MEAT, FISH, EGGS, FRUIT, VEGETABLES, EDIBLE SEEDS; CHEMICAL RIPENING OF FRUIT OR VEGETABLES; THE PRESERVED, RIPENED, OR CANNED PRODUCTS"
    assert funcao(
        instance.group) == "Preservation of edible seeds, e.g. cereals"
    assert funcao(
        instance.subgroup) == "Apparatus for preserving using liquids"


def test_description():
    assert instance.description.section == "HUMAN NECESSITIES"
    assert instance.description.classe == "FOODS OR FOODSTUFFS; THEIR TREATMENT, NOT COVERED BY OTHER CLASSES"
    assert instance.description.subclass == "PRESERVING, e.g. BY CANNING, MEAT, FISH, EGGS, FRUIT, VEGETABLES, EDIBLE SEEDS; CHEMICAL RIPENING OF FRUIT OR VEGETABLES; THE PRESERVED, RIPENED, OR CANNED PRODUCTS"
    assert instance.description.group == "Preservation of edible seeds, e.g. cereals"
    assert instance.description.subgroup == "Apparatus for preserving using liquids"
