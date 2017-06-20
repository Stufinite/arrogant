from distutils.core import setup

setup(
    name = 'arrogant',
    packages = ['arrogant'],
    version = '1.8',
    description = 'An API for 企業徵才.',
    author = 'davidtnfsh',
    author_email = 'davidtnfsh@gmail.com',
    url = 'https://github.com/Stufinite/arrogant',
    download_url = 'https://github.com/Stufinite/arrogant/archive/v1.8.tar.gz',
    keywords = ['arrogant', 'campass'],
    classifiers = [],
    license='GPL3.0',
    install_requires=[
        'djangoApiDec',
        'pyprind'
    ],
    zip_safe=True,
)
