from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='django-email-processing',
      version=version,
      description="Incoming email processing system",
      long_description="",
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author_email='iyarslv@gmail.com',
      url='',
      license='Apache',
      packages=find_packages('email_processing'),
      package_dir={'':'email_processing'},
      include_package_data=True,
      zip_safe=False,
      extras_require = dict(
        test = []
        ),
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      dependency_links = [],
      )
