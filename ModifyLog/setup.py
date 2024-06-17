from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
version = {}
with open(os.path.join(here, 'mlog','version.py')) as fp:
    exec(fp.read(), version)

print("[INFO] Modify Logging")
setup(
    name='mlog',
    version=version['__version__'],
    author='Chau Thai Nguyen',
    author_email= 'nguyenbku97@gmail.com',
    maintainer='Chau Thai Nguyen',
    packages= find_packages(include=['mlog']),
    install_requires=['pyyaml',]
)