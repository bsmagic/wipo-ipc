from wipo_ipc import description

section = "A"
classe = "A23"
subclass = "A23B"
group = "A23B0009000000"
subgroup = "A23B0009320000"


def test_query_description():
    funcao = description.query_description
    assert funcao(section) == "HUMAN NECESSITIES"
    assert funcao(
        classe) == "FOODS OR FOODSTUFFS; THEIR TREATMENT, NOT COVERED BY OTHER CLASSES"
    assert funcao(subclass) == "PRESERVING, e.g. BY CANNING, MEAT, FISH, EGGS, FRUIT, VEGETABLES, EDIBLE SEEDS; CHEMICAL RIPENING OF FRUIT OR VEGETABLES; THE PRESERVED, RIPENED, OR CANNED PRODUCTS"
    assert funcao(group) == "Preservation of edible seeds, e.g. cereals"
    assert funcao(subgroup) == "Apparatus for preserving using liquids"
