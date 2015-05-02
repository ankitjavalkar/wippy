#! /usr/bin/env python
from setuptools import setup, find_packages

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(name='wippy',
      author='Ankit Javalkar',
      author_email='ankitjavalkar@gmail.com',
      description='Random Work In Progress message generator for Python',
      license='GPLv3',
      version='0.0.1',
      url='https://github.com/ankitjavalkar/wippy',
      packages=find_packages(),
      include_package_data=True,
      classifiers=CLASSIFIERS,
      platforms=['any'])
