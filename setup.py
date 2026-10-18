from setuptools import setup, find_packages

setup(
    name = "io_comp",
    version = "0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts":[
            "Comp-calendar=io_comp.app:main",
        ],
    },
)