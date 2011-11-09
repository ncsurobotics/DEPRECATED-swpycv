
from distutils.core import setup,Extension

setup(
    name='swpycv',
    version='1.0',
    author='Chris Thunes',
    author_email='cmthunes@ncsu.edu',
    description='Helper functions for interfacing C libraries using OpenCV through ctypes',

    packages=['swpycv'],
    package_dir={'swpycv': 'swpycv'},
    package_data={'swpycv': ['swpycv.so']}
    )
