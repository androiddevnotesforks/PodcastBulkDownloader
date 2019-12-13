#!/usr/bin/env python

from setuptools import setup

version = '0.1'

setup(name='Podcast Bulk Downloader',
      version=version,
      description='Simple software for downloading all the episodes of a podcast',
      author='Cyril Novel',
      author_email='podcast.bulk@kosmon.fr',
      install_requires=['requests', 'bs4', 'pytest', 'pytest-cov'],
      packages=['src'],
      scripts=['src/app.py', 'src/bulk_downloader.py', 'src/callback.py']
      )
