========
 DoJSON
========

.. currentmodule:: dojson

.. image:: https://img.shields.io/travis/tu-graz-library/dojson.svg
        :target: https://travis-ci.org/tu-graz-library/dojson

.. image:: https://img.shields.io/coveralls/tu-graz-library/dojson.svg
        :target: https://coveralls.io/r/tu-graz-library/dojson

.. image:: https://img.shields.io/github/tag/tu-graz-library/dojson.svg
        :target: https://github.com/tu-graz-library/dojson/releases

.. image:: https://img.shields.io/pypi/dm/dojson.svg
        :target: https://pypi.python.org/pypi/dojson

.. image:: https://img.shields.io/github/license/tu-graz-library/dojson.svg
        :target: https://github.com/tu-graz-library/dojson/blob/master/LICENSE


About
=====

DoJSON is a simple Pythonic JSON to JSON converter.

Installation
============

DoJSON is on PyPI so all you need is:

.. code-block:: console

    $ pip install dojson

Documentation
=============

Documentation is readable at https://dojson.readthedocs.io/ or
it can be built using Sphinx:

.. code-block:: console

    $ pip install dojson[docs]
    $ python setup.py build_sphinx

Testing
=======

Running the test suite is as simple as:

.. code-block:: console

    $ python setup.py test

Example
=======

A simple example on how to convert MARCXML to JSON:

.. code:: python

    from dojson.contrib.marc21.utils import create_record, split_stream
    from dojson.contrib.marc21 import marc21
    [marc21.do(create_record(data)) for data in split_stream(open('/tmp/data.xml', 'r'))]
