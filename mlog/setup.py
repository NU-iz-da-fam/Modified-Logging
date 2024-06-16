from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
version = {}
with open(os.path.join(here, "version.py")) as fp:
    exec(fp.read(), version)

print("[INFO] Modify Logging")
setup(
    name='mlog',
    version=version['__version__'],
    author='Chau Thai Nguyen',
    maintainer='Chau Thai Nguyen | nguyenbku97@gmail.com',
    packages= find_packages(include=['modlog']),
    install_requires=['pyyaml',]
)