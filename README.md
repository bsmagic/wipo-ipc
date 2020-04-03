[![PyPI version shields.io](https://img.shields.io/pypi/v/wipo-ipc.svg)](https://pypi.org/project/wipo-ipc/)
[![PyPI license](https://img.shields.io/pypi/l/wipo-ipc.svg)](https://pypi.org/project/wipo-ipc/)
[![Documentation Status](https://readthedocs.org/projects/wipo-ipc/badge/?version=latest)](http://wipo-ipc.readthedocs.io/?badge=latest)

# WIPO-IPC

A library to work with the International Patent Classification(IPC) from the World Intellectual Property Organization(WIPO)

## Getting Started

### Installing

```
pip install wipo-ipc
```

### Basic Usage

```python
>>> from wipo_ipc import Ipc

>>> my_ipc = Ipc("A23B0009320000")

>>> my_ipc.classe
'A23'
>>> my_ipc.description
Description(section='HUMAN NECESSITIES', classe='FOODS OR FOODSTUFFS; THEIR TREATMENT, NOT COVERED BY OTHER CLASSES', subclass='PRESERVING, e.g. BY CANNING, MEAT, FISH, EGGS, FRUIT, VEGETABLES, EDIBLE SEEDS; CHEMICAL RIPENING OF FRUIT OR VEGETABLES; THE PRESERVED, RIPENED, OR CANNED PRODUCTS', group='Preservation of edible seeds, e.g. cereals', subgroup='Apparatus for preserving using liquids')
>>> my_ipc.description.classe
'FOODS OR FOODSTUFFS; THEIR TREATMENT, NOT COVERED BY OTHER CLASSES'
```

## Contributing

```
git clone git@github.com:mateusrangel/wipo-ipc.git
cd wipo-ipc
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

## Running the tests

```
pytest tests/
```

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/mateusrangel/wipo-ipc/tags). 

## Authors

* [**Mateus Rangel**](https://github.com/mateusrangel) - *Initial work*

See also the list of [contributors](https://github.com/mateusrangel/wipo-ipc/contributors) who participated in this project.

## License

This project is licensed under the GNU GPL v3 License - see the [LICENSE.md](LICENSE) file for details

