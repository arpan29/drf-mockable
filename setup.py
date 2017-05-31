from setuptools import setup
setup(
    name = 'drf_mockable',
    packages = ['drf_mockable'], # this must be the same as the name above
    version = '0.0.2',
    description = 'A package to help in building mockable APIs based over Django Rest Framework (DRF)',
    author = 'Arpan Gupta',
    author_email = 'arpan29@gmail.com',
    url = 'https://github.com/arpan29/drf-mockable', # use the URL to the github repo
    download_url = 'https://github.com/arpan29/drf-mockable/archive/master.zip', # I'll explain this in a second
    keywords = ['mock', 'DRF', 'mockable', 'APIs', 'REST', 'Django'], # arbitrary keywords
    classifiers = [],
    license = 'MIT',
    install_requires=[
        'Django',
        'djangorestframework',
    ],
    zip_safe=False
)