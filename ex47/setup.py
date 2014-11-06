
try:
	from setuptools import setup
except ImportError:
	from disutils.core import setup

config = [
	'description': 'My Project',
	'author': 'David Lee',
	'url': '#',
	'download_url': '#',
	'author_email': 'xarchaiax@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['FirstProject'],
	'scripts': [],
	'name': 'projectname'
]

setup(**config)