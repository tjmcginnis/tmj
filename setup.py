try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Two Minute Journal',
    'author': 'Tyler McGinnis',
    'url': '',
    'download_url': '',
    'author_email': 'tylermcginnis@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['twominutejournal'],
    'scripts': [],
    'name': 'twominutejournal'
}

setup(**config)
