from distutils.core import setup

setup(
    name = 'arrogant',
    packages = ['arrogant'],
    version = '1.6',
    description = 'An API for 企業徵才.',
    author = 'davidtnfsh',
    author_email = 'davidtnfsh@gmail.com',
    url = 'https://github.com/Stufinite/arrogant',
    download_url = 'https://github.com/Stufinite/arrogant/archive/v1.6.tar.gz',
    keywords = ['arrogant', 'campass'],
    classifiers = [],
    license='GPL3.0',
    install_requires=[
        'djangoApiDec',
    ],
    zip_safe=True,
)
