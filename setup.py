#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

import david

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()
                if not i.startswith('#') and i.strip()]

print REQUIREMENTS

dependency_links = ['http://pypi.douban.com/simple/']

classifiers = ["Development Status :: 4 - Beta",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Framework :: Flask",
               'Programming Language :: Python',
               "Programming Language :: Python :: 2.7",
               "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
               'Topic :: Software Development :: Libraries :: Python Modules']

try:
    long_description = open('README.md').read()
except:
    long_description = david.__description__

setup(name='david',
      version=david.__version__,
      description=david.__description__,
      long_description=long_description,
      classifiers=classifiers,
      keywords='david cms flask publishing mysql',
      author=david.__author__,
      author_email=david.__email__,
      license=david.__license__,
      packages=find_packages(exclude=('doc', 'docs',)),
      namespace_packages=['david'],
      package_dir={'david': 'david'},
      install_requires=REQUIREMENTS,
      dependency_links=dependency_links,
      scripts=['david/bin/david-admin.py'],
      include_package_data=True,
      test_suite='runtests')
