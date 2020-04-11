************
ShareAndCare
************

Help to share the excess food among needy people

Prerequisites
=============

- python 3.6

Setup
=====

Fork this repo and clone it to your local machine. Then follow
the below instructu -

1. Create a new virtual environment and install the necessary
packages -

.. code-block:: shell

   $ pipenv install

2. Start the virtual environment.

.. code-block:: shell

   $ pipenv shell

3. Start the development server.

.. code-block:: shell

   $ pipenv run server

Linter
======

After writing your code run the below commands -

To sort all python imports -

.. code-block:: shell

   $ pipenv run isort

To run the python linter(flake8) -

.. code-block:: shell

   $ pipenv run flake8

Tests
=====

All your code should pass the test -

.. code-block:: shell

   $ pipenv run test

Build docs
==========

First start the virtual environment and go inside
the docs folder. And run the below command -

.. code-block:: shell

   $ make html
