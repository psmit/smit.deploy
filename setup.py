#!/usr/bin/env python

from setuptools import setup

setup(name='smit.deploy',
      version='0.0.1dev',
      description='Tool for deploying web app',
      author='Peter Smit',
      author_email='peter@smitmail.eu',
      packages=['smit'],
      package_dir={'': 'src'},
      install_requires=[],
      entry_points = dict(console_scripts=[
        'launchserver = smit.deploy.deploy:run',
        ])
      )
