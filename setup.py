try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Skeeter IOC Scrapper',
    'author': 'Bhavna Soman',
    'url': 'https://github.com/bsoman3/skeeter',
    'version': '0.1',
    'install_requires': [
        'nose',
        'nltk', 
        'textract', 
        'tldextract',
    ],
    'packages': [],
    'scripts': [],
    'name': 'skeeter'
}

setup(**config)
