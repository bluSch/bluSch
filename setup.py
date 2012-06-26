#!/usr/bin/env python
 
from setuptools import setup
 
VERSION = '0.0.1'
 
setup(
  name = 'bluSch',
  version = VERSION,
  descriptionl = 'the source of bluSch.net',
  author = 'bluSch seVen',
  author_email = 'b@bluSch.net',
 
  packages = ['bluSite',],
  package_dir = {'': 'src/bluSch'},
 
  install_requires = [
    'django == 1.4',
  ]
)
