__version__ = '1.0.1'

from setuptools import setup, find_packages

setup (
       name='python-android',
       version=__version__,
       author='Chris Soyars',
       author_email='me@ctso.me',
       description='A collection of tools for interacting with Android builds.',
       url='http://github.com/ctso/python-android',

       packages=find_packages('src'),
       package_dir={'':'src'},

       install_requires=[],

       entry_points={
            'console_scripts':[
                "bootinfo = android.command:main",
            ]
       },
)
