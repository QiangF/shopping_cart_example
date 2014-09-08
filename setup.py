#!/usr/bin/env python

# setuptools is not actually required to install.
from distutils.core import setup

__AUTHOR__ = 'David Halter'
__AUTHOR_EMAIL__ = 'davidhalter88@gmail.com'

readme = open('README.rst').read() + '\n\n' + open('CHANGELOG.rst').read()

import cart

setup(name='cart',
      version=cart.__version__,
      description='A shopping cart.',
      author=__AUTHOR__,
      author_email=__AUTHOR_EMAIL__,
      maintainer=__AUTHOR__,
      maintainer_email=__AUTHOR_EMAIL__,
      url='https://github.com/davidhalter-archive/cart',
      license='MIT',
      keywords='shopping cart',
      long_description=readme,
      packages=['cart'],
      platforms=['any'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
      ],
      )
