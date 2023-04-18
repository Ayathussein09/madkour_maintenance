from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in madkour_maintenance/__init__.py
from madkour_maintenance import __version__ as version

setup(
	name="madkour_maintenance",
	version=version,
	description="madkour_maintenance",
	author="madkour",
	author_email="123",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
