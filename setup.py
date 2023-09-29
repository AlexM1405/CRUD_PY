
from setuptools import setup

setup(
    name="sv",
    version="0.1",
    py_modules=["sv"],
    intall_requires =[
        "Click",
    ],
    entry_points ="""
        [console_scripts]
        sv= sv:cli
    """,
)