import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

requests = 'requests >= 0.8.8'
install_requires = [requests]

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'nsone'))
from version import VERSION

setup(
    name='nsone',
    version=VERSION,
    description='NSONE python bindings',
    author='NSONE',
    author_email='support@nsone.net',
    url='https://nsone.net/',
    packages=['nsone'],
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])