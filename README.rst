==============
Django JET 3.0
==============

This repo was forked from geex-arts/django-jet. It was updated to add Django 3 compatibility.

Please ensure you follow all conditions of the original license.

Code Changes
----------------
- Removed 'python2_compatibility' decorators and imports
- Converted 'admin_static' refs to 'static'
- Modified this README to reflect new installation process


========
Read Me
========

**Modern template for Django admin interface with improved functionality**


Django JET has two kinds of licenses: open-source (AGPLv3) and commercial. Please note that using AGPLv3
code in your programs make them AGPL compatible too. So if you don't want to comply with that we can provide you a commercial
license (visit Home page). The commercial license is designed for using Django JET in commercial products
and applications without the provisions of the AGPLv3.
    
* Documentation: http://jet.readthedocs.org/
* libi.io http://libi.io/library/1683/django-jet
* PyPI: https://pypi.python.org/pypi/django-jet

Why Django JET?
===============

* New fresh look
* Responsive mobile interface
* Useful admin home page
* Minimal template overriding
* Easy integration
* Themes support
* Autocompletion
* Handy controls

Installation
============

* Clone and build Django JET:

.. code:: bash

    git clone https://github.com/IntrospectData/django-jet.git
    cd django-jet
    python setup.py sdist bdist

.. code:: python

    pip install ./dist/django-jet-3.0.tar.gz


* Add 'jet' application to the INSTALLED_APPS setting of your Django project settings.py file (note it should be before 'django.contrib.admin'):

.. code:: python

    INSTALLED_APPS = (
        ...
        'jet',
        'django.contrib.admin',
    )
        
* Make sure ``django.template.context_processors.request`` context processor is enabled in settings.py (Django 1.8+ way):

.. code:: python

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    ...
                    'django.template.context_processors.request',
                    ...
                ],
            },
        },
    ]

* Add URL-pattern to the urlpatterns of your Django project urls.py file (they are needed for related–lookups and autocompletes):

.. code:: python

    urlpatterns = patterns(
        '',
        url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
        url(r'^admin/', include(admin.site.urls)),
        ...
    )

* Create database tables:

.. code:: python

    python manage.py migrate jet
        
* Collect static if you are in production environment:

.. code:: python

        python manage.py collectstatic
        
* Clear your browser cache

Dashboard installation
======================

.. note:: Dashboard is located into a separate application. So after a typical JET installation it won't be active.
          To enable dashboard application follow these steps:

* Add 'jet.dashboard' application to the INSTALLED_APPS setting of your Django project settings.py file (note it should be before 'jet'):

.. code:: python

    INSTALLED_APPS = (
        ...
        'jet.dashboard',
        'jet',
        'django.contrib.admin',
        ...
    )

* Add URL-pattern to the urlpatterns of your Django project urls.py file (they are needed for related–lookups and autocompletes):

.. code:: python

    urlpatterns = patterns(
        '',
        url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
        url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
        url(r'^admin/', include(admin.site.urls)),
        ...
    )

* **For Google Analytics widgets only** install python package:

.. code::

    pip install google-api-python-client==1.4.1

* Create database tables:

.. code:: python

    python manage.py migrate dashboard
    # or
    python manage.py syncdb

* Collect static if you are in production environment:

.. code:: python

        python manage.py collectstatic



