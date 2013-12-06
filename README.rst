cookiecutters
==========================

.. image:: https://api.travis-ci.org/rpedigoni/cookiecutters.cc.png
        :target: https://travis-ci.org/rpedigoni/cookiecutters.cc

Installation
------------

Create a virtualenv (use ``virtualenvwrapper``): ::

    mkvirtualenv cookiecutters


Install requirements via ``pip``: ::

    pip install django/requirements/development.txt


Create database tables: ::

    # on django/cookiecutters
    ./manage.py syncdb --all --settings=settings.development


Run the project: ::

    # on django/cookiecutters
    ./manage.py runserver --settings=settings.development


Tests
-----

To run the test suite, execute: ::

    make test


To show coverage details (in HTML), use: ::

    make test html
