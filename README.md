# Django client-side dependencies app

[![PyPI Version](https://img.shields.io/pypi/v/django-client-side.svg)][1]
[![Tests](https://github.com/powderflask/django-client-side/actions/workflows/pytest.yaml/badge.svg)][3]

[1]: <https://pypi.python.org/pypi/django-client-side>
[3]: <https://github.com/powderflask/django-client-side/actions/workflows/pytest.yaml>

Manage client-side JS / CSS dependencies for your django project.

 * Version: 0.3.1
 * Author: powderflask
 * Source: https://github.com/powderflask/django-client-side
 * [MIT License](https://github.com/powderflask/django-client-side/blob/master/LICENSE)


## OVERVIEW:

 * Maintain client-side dependencies in one place (i.e., not scattered in templates).
 * Provides testable, executable client-side app dependencies set.
 * Template tags used to pull JS / CSS dependencies into templates.
 * Local static resources and/or from CDN. 
 * Use any client-side build tools or none - demo app uses npm as JS package manager and build tool.
 * conditional dependencies for different build environments

### Dependencies:
 * python 3
 * django


## Quick start

* `pip install https://github.com/powderflask/django-client-side.git`

 1) Add `client_side` to `INSTALLED_APPS`
    ```
    INSTALLED_APPS = [
        ...
        'client_side',
    ]
    ```

 2) define client-side dependency set (*see tests.dependencies for example*)
 
 3) in settings.py, configure `CLIENT_SIDE_DEPENDENCIES` setting:
    ```
    CLIENT_SIDE_DEPENDENCIES = 'myproject.client_side.dependencies.DEPENDENCIES'  # dotted-path to your dependency sets
    ```
    (may be a dotted-path to a `DependencySets` object or specify the `DependencySets` object directly in settings.)
 4) Use `{% stylesheet <name> %}`  and  `{% javascript <name> %}` in your templates to pull in sets of dependencies
 
 5) Update your client-side dependency sets any time without ever touching your templates! 

## Guide
### Define Client-Side Components
```
 from client_side.component import Component, DependencySets, Script, Stylesheet
```

Define a `Component` for each dependency, with zero or more `Script` elemenets and/or zero or more `Stylesheet` elements:
```
component = Component(
    Script(url="https://example.com/component.js", sri="sha384-js-sri-here"),
    Stylesheet(url="https://example.com/component.css", sri="sha384-css-sri-here"),
)
```

Swap components for different environments, pass `static=True` for dependencies loaded from `static` files:
```
lib_common = Component(
    Script(url="lib/common.js" if settings.DEBUG else "lib/common.min.js", static=True),
    Stylesheet(
        url="lib/common.css" if settings.DEBUG else "lib/common.min.css", static=True
    ),
)
```

### Group Components into Logical Dependency Sets

Define one or more `DependencySets` with logical component groups:
```
DEPENDENCIES = DependencySets(
    core=(component, lib_common,),
    debug=(debug_toolbar, hijack), 
)
```

### Include DependencySets in Templates
```
{% load dependency_tags %}
...
      {% stylesheet 'core' %}
...
      {% javascript 'core' %}
      {% if debug %}
        {% javascript 'debug' %}
      {% endif %}  
```


### Acknowledgments
Special thanks to BC Hydro, [Chartwell](https://crgl.ca/),
and all [Contributors](https://github.com/powderflask/django-client-side/graphs/contributors)

## For Developers
 * `> pip install -r reqirements_dev.txt`

### Tests
 * `> pytest`
 * `> tox`

### Code Style
 * `> isort`
 * `> black`
 * `> flake8`

### Versioning
 * [Semantic Versioning](https://semver.org/)
 * `> bumpver` 

### Build / Deploy Automation
 * [invoke](https://www.pyinvoke.org/)
   * `> invoke -l` 
 * [GitHub Actions](https://docs.github.com/en/actions) (see [.github/workflows](https://github.com/powderflask/django_document_catalogue/tree/master/.github/workflows))
