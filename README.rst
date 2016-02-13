This is a fork of `django-budget <https://github.com/toastdriven/django-budget>`_.

It has been modified to work with django 1.9, and also to function as a
standalone app.  To get a functioning app, you have to run these commands:

.. code-block:: bash

    git clone https://github.com/codypiersall/django-budget.git
    cd django-budget
    python manage.py makemigrations budget categories transactions
    python manage.py migrate
    python manage.py collectstatic
    python manage.py runserver

After running these commands once, you can run the app in the future by just
running

.. code-block:: bash

    python manage.py runserver

To look at your budget stuff, go in your browser to
``http://127.0.0.1:8000/budget/``.  Happy budgeting!

=============
django-budget
=============

``django-budget`` is a simple budgeting application for use with Django. It is
designed to manage personal finances. We used it to replace a complicated Excel
spreadsheet that didn't retain all the details we wanted.

It was implemented in Django based on familiarity, quick time to implement and
the premise that it could be accessible everywhere. In practice, we run this
locally (NOT on a publicly accessible website).


A Note About Security
=====================

It is recommended that anyone using this application add further security by
either protecting the whole app with HTTP Auth, wrap the views with the
``login_required`` decorator, run it on a local machine or implement similar
protections. This application is for your use and makes no assumptions about
how viewable the data is to other people.


Requirements
============

``django-budget`` requires:

* Python 2.3+
* Django 1.0+


Installation
============

* Either copy/symlink the budget app into your project or place it somewhere on
  your ``PYTHONPATH``.
* Add the ``budget.categories``, ``budget.transactions`` and ``budget`` apps to
  your ``INSTALLED_APPS``.
* Run ``./manage.py syncdb``.
* Add ``(r'^budget/', include('budgetproject.budget.urls')),`` to your
  ``urls.py``.


About The Templates/Media
=========================

The templates provided are for reference only and ARE NOT SUPPORTED! Please do
not submit bugs or feature requests for them. You will likely have to create
your own templates or at least heavily modify these templates to adapt them to
your own uses. Everything within the templates is either original or MIT
licensed.
