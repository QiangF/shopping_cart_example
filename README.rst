###################################################
Jedi - an awesome autocompletion library for Python
###################################################

.. image:: https://secure.travis-ci.org/davidhalter-archive/cart.png?branch=master
    :target: http://travis-ci.org/davidhalter-archive/cart
    :alt: Travis-CI build status

.. image:: https://coveralls.io/repos/davidhalter-archive/cart/badge.png?branch=master
    :target: https://coveralls.io/r/davidhalter-archive/cart
    :alt: Coverage Status

.. image:: https://pypip.in/d/jedi/badge.png
    :target: https://crate.io/packages/jedi/
    :alt: Number of PyPI downloads

.. image:: https://pypip.in/v/jedi/badge.png
    :target: https://crate.io/packages/jedi/
    :alt: Latest PyPI version

``cart`` is a small project to show how setting up a proper Python project
works.





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


.. _jedi-vim: https://github.com/davidhalter-archive/cart-vim
