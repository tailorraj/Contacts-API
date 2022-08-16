from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in whatsapp_notification/__init__.py
from whatsapp_notification import __version__ as version

setup(
	name='whatsapp_notification',
	version=version,
	description='Whatsapp Notification',
	author='Nikhil Gandhi',
	author_email='gandhi.nikhil3@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
