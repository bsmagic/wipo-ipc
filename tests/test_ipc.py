from wipo_ipc import Ipc
import pytest

ipc_code = "A23B0009320000"

instance_section_only = Ipc("A")
instance = Ipc(ipc_code)


def test_invalid_ipc():
    with pytest.raises(ValueError):
        invalid_instance = Ipc("Z")


def test_equality():
    assert instance == Ipc(ipc_code)


def test_repr():
    assert repr(instance) == ipc_code


def test_partes():
    assert instance.section.code == "A"
    assert instance.classe.code == "A23"
    assert instance.subclass.code == "A23B"
    assert instance.group.code == "A23B0009000000"
    assert instance.subgroup.code == "A23B0009320000"


def test_get_descriptions():
    assert instance.section.description == "HUMAN NECESSITIES"
    assert instance.classe.description == "FOODS OR FOODSTUFFS; THEIR TREATMENT, NOT COVERED BY OTHER CLASSES"
    assert instance.subclass.description == "PRESERVING, e.g. BY CANNING, MEAT, FISH, EGGS, FRUIT, VEGETABLES, EDIBLE SEEDS; CHEMICAL RIPENING OF FRUIT OR VEGETABLES; THE PRESERVED, RIPENED, OR CANNED PRODUCTS"
    assert instance.group.description == "Preservation of edible seeds, e.g. cereals"
    assert instance.subgroup.description == "Apparatus for preserving using liquids"
