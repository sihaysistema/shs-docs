from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in shs_docs/__init__.py
from shs_docs import __version__ as version

setup(
	name="shs_docs",
	version=version,
	description="Documentación",
	author="Si Hay Sistema",
	author_email="m.m@sihaysistema.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
