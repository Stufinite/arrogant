from distutils.core import setup

setup(
    name = 'arrogant',
    packages = ['arrogant'],
    package_dir={'arrogant':'arrogant'},
    package_data={'arrogant':['migrations/*', 'school2location.json', 'dept2job.json']},
    version = '2.5',
    description = 'An API for 企業徵才.',
    author = 'davidtnfsh',
    author_email = 'davidtnfsh@gmail.com',
    url = 'https://github.com/Stufinite/arrogant',
    download_url = 'https://github.com/Stufinite/arrogant/archive/v2.5.tar.gz',
    keywords = ['arrogant', 'campass'],
    classifiers = [],
    license='GPL3.0',
    install_requires=[
        'djangoApiDec',
        'pyprind'
    ],
    zip_safe=True,
)
