###################################
Cart - A simple shopping cart demo.
###################################

.. image:: https://secure.travis-ci.org/davidhalter-archive/cart.png?branch=master
    :target: http://travis-ci.org/davidhalter-archive/cart
    :alt: Travis-CI build status

.. image:: https://coveralls.io/repos/davidhalter-archive/cart/badge.png?branch=master
    :target: https://coveralls.io/r/davidhalter-archive/cart
    :alt: Coverage Status

``cart`` is a small project to show how setting up a proper Python project
works.


Thoughts
========

- Not modifying the actual quantities is strange: In a store with a three for
  two offer, you usually get three automatically if you buy two. Here we have
  to buy three to actually get three for the price of two. If we buy two, we
  will only receive two. However that's ok I guess, since there's no API for
  the actual quantities.
- Offers are mostly abstract. You could implement real offers for e.g.
  snickers. But abstract offers make more sense, IMHO.


Possible Improvements
=====================

- ``devpi`` would be great to test the package deployment.
- Limit development to pure Python 3 and use function annotations to describe
  the API types (instead of docstrings).
- Docs. No docs typically implies failed Sphinx references. (Which are used in
    this project.


Installation
============

Once this package is added to PyPI, you will be able to use::

    pip install cart

For now, you can install this package by using::

    pip install -e .


Feature Support and Caveats
===========================

You can run ``cart`` on cPython 2.7, cPython 3.3+. There's experimental support
for pypy.


Testing
=======

The test suite depends on ``tox`` and ``pytest``::

    pip install tox pytest

To run the tests for all supported Python versions::

    tox

If you want to test only a specific Python version (e.g. Python 2.7), it's as
easy as ::

    tox -e py27

Tests are also run automatically on `Travis CI
<https://travis-ci.org/davidhalter-archive/cart/>`_.


If you ever struggle to work test driven, use this::

    watch -n 1 --color "py.test-3.4 --color=yes| tail -n 20"
