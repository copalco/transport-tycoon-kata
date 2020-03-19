from setuptools import find_packages
from setuptools import setup

setup(
    name='transport-tycoon',
    version='1.0.0',
    packages=find_packages(include='transport_tycoon*',),
    include_package_data=True,
    zip_safe=False,
)
