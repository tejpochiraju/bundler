from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in bundler/__init__.py
from bundler import __version__ as version

setup(
	name='bundler',
	version=version,
	description='Frappe App For Bundler',
	author='Tej Pochiraju',
	author_email='hi@tejpochiraju.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
