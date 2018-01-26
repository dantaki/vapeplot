import os
from setuptools import setup
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
    name = "vapeplot",
    version = "0.0.1",
    author = "Danny Antaki",
    author_email = "dantaki@ucsd.edu",
    description = ("matplotlib extension for vaporwave aesthetics"),
    license = "GPLv2",
    keywords = "vaporwave matplotlib",
    url = "https://github.com/dantaki/vapeplot/",
    packages=['vapeplot'],
    package_dir={'vapeplot':'vapeplot/'},
    long_description=read('README.md'),
    install_requires=['matplotlib'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Topic :: Multimedia :: Graphics',
    ]

)

