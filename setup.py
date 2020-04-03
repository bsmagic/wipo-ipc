import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wipo-ipc",
    version="1.0.0",
    author="Mateus Rangel",
    author_email="mateusmrangel@hotmail.com",
    description="A library to work with the International Patent Classification(IPC) from the World Intellectual Property Organization(WIPO)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mateusrangel/wipo-ipc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True
)
