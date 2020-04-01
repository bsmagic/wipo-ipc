from wipo_ipc import ipc

ipc_code = "A23B0009320000"
instance = ipc.Ipc(ipc_code)


def test_partes():
    assert instance.section == "A"
    assert instance.classe == "A23"
    assert instance.subclass == "A23B"
    assert instance.group == "A23B0009000000"
    assert instance.subgroup == "A23B0009320000"


def test_get_descriptions():
    assert instance.description.section == "HUMAN NECESSITIES"
    assert instance.description.classe == "FOODS OR FOODSTUFFS; THEIR TREATMENT, NOT COVERED BY OTHER CLASSES"
    assert instance.description.subclass == "PRESERVING, e.g. BY CANNING, MEAT, FISH, EGGS, FRUIT, VEGETABLES, EDIBLE SEEDS; CHEMICAL RIPENING OF FRUIT OR VEGETABLES; THE PRESERVED, RIPENED, OR CANNED PRODUCTS"
    assert instance.description.group == "Preservation of edible seeds, e.g. cereals"
    assert instance.description.subgroup == "Apparatus for preserving using liquids"
