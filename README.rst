Nonovium Video Backend
======================

Your platform, your videos, your data

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
    :alt: Black code style
.. image:: https://github.com/SuperSuperStore/NonoviumVideoBackend/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/SuperSuperStore/NonoviumVideoBackend/actions/workflows/ci.yml
    :alt: Continuous integration


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

    $ mypy nonovium_video_backend

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html

Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd nonovium_video_backend
    celery -A config.celery_app worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check `cookiecutter-django Docker documentation`_ for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

.. _mailhog: https://github.com/mailhog/MailHog

Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

Deployment
----------

The following details how to deploy this application.

Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html

Helpful ZSH Commands
--------------------

.. code-block:: bash

    ######
    # Docker
    ######
    # When installing for the first time:
    alias dkbld="docker-compose -f local.yml build --no-cache"
    # Start the containers:
    alias dkup="docker-compose -f local.yml up"
    # Stop the containers:
    alias dkdown="docker-compose -f local.yml down"
    # Stop and remove/delete the containers (Does not remove postgres container but dumps the database):
    alias dkdownclean="docker-compose -f local.yml down --volumes --rmi all"
    ######
    # Docker Django Container and main App Container)
    ######
    alias dkpysupu="docker-compose -f local.yml run --rm django python manage.py createsuperuser --username admin --email admin@email.com"
    alias dkpy="docker-compose -f local.yml run --rm django python manage.py"
    alias dkpyrun="docker-compose -f local.yml run --rm django python manage.py runserver"
    alias dkpymkmig="docker-compose -f local.yml run --rm django python manage.py makemigrations"
    alias dkpymig="docker-compose -f local.yml run --rm django python manage.py migrate"
    alias dkpyshell="docker-compose -f local.yml run --rm django python manage.py shell"
    alias dkpytest="docker-compose -f local.yml run --rm django python manage.py test"
    alias dkpycoverage="docker-compose -f local.yml run --rm django python manage.py test --coveragetest"
    alias dkpydump="docker-compose -f local.yml run --rm django python manage.py dumpdata --indent=2"
    alias dkpyload="docker-compose -f local.yml run --rm django python manage.py loaddata"
    alias dkpyblack="docker-compose -f local.yml run --rm django python -m black ."
    alias dkdjstartapp="docker-compose -f local.yml run --rm django django-admin startapp"
    alias dkpycel="docker-compose -f local.yml run --rm django celery"
    alias dkpystartapp="docker-compose -f local.yml run --rm django python manage.py startapp"
    ######
    # Docker Postgres
    ######
    alias dkpqlstart="docker-compose -f local.yml run --rm postgres sudo service postgresql start"
    alias dkpqlstop="docker-compose -f local.yml run --rm postgres sudo service postgresql stop"
    alias dkpqlrestart="docker-compose -f local.yml run --rm postgres sudo service postgresql restart"
    alias dkpqlstatus="docker-compose -f local.yml run --rm postgres sudo service postgresql status"
    alias dkpqlbackup="docker-compose -f local.yml exec postgres backup"
    ######
    # Docker Celery
    ######
    alias dkcel="docker-compose -f local.yml run --rm celery"



.. code-block:: bash
    test





Acknowledgements
----------------

Cookiecutter
^^^^^^^^^^^^^

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
    :target: https://github.com/pydanny/cookiecutter-django/
    :alt: Cookiecutter Django
