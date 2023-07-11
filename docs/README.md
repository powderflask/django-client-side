# Django client-side dependencies app

[![PyPI Version](https://img.shields.io/pypi/v/django_client_side.svg)](https://pypi.python.org/pypi/django_client_side)

[![Documentation Status](https://readthedocs.org/projects/django-client-side/badge/?version=latest)](https://django-client-side.readthedocs.io/en/latest/?version=latest)


Manage client-side JS / CSS dependencies for your django project.

* Version: 0.2.0
* Author: powderflask
* Author URI: https://github.com/powderflask/django-client-side
* License: MIT see [LICENSE](../LICENSE)

OVERVIEW:
--------

* Maintain client-side dependencies in one place (i.e., not scattered in templates).
* Provides testable, executable client-side app dependencies set.
* Template tags used to pull JS / CSS dependencies into templates.
* Local static resources and/or from CDN.
* Use any client-side build tools or none - demo app uses npm as JS package manager and build tool.
* conditional dependencies for different build environments

Dependencies:

* python 3
* django 2


Quick start
-----------

* `pip install https://github.com/powderflask/django-client-side.git`
* `python3 setup.py test`   (to run app test suite)

1) Add `'client_side'` to `INSTALLED_APPS`  (and `django.contrib.staticfiles` if you use local static resources)
   ```python
   INSTALLED_APPS = [
       ...
       'client_side',
       ...
   ]
   ```

2) define client-side dependency set (see `demo.dependencies` for example)

3) in settings.py, configure `CLIENT_SIDE_DEPENDENCIES` setting:
   ```python
   CLIENT_SIDE_DEPENDENCIES = 'myproject.client_side.dependencies.DEPENDENCIES'  # dotted-path to your dependency sets
   ```
   (may be a dotted-path to a dict or specify the dependency set dict directly in settings.)
4) Use `{% stylesheet <name> %}`  and  `{% javascript <name> %}` in your templates to pull in sets of dependencies

5) Update your client-side dependency sets any time without ever touching your templates! 
