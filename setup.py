from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='django-email-processing',
      version=version,
      description="Incoming email processing system",
      long_description="",
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        ],
      author = 'Yaroslav D.',
      author_email='iyarslv@gmail.com',
      url='',
      packages=['email_processing'],
      include_package_data=True,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """
      )
