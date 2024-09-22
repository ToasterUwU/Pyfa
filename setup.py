import yaml
from setuptools import find_packages, setup

with open("version.yml", "r") as f:
    version = yaml.load(f, yaml.SafeLoader)["version"].replace("v", "")

setup(
    name="Pyfa",
    version=version,
    # Modules to import from other scripts:
    packages=find_packages(),
    # Executables
    scripts=["pyfa.py"],
    script_name="pyfa"
)
