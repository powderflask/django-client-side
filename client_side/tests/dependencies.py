"""
Test dependencies for client-side tests
"""
from django.conf import settings

from client_side.component import Component, DependencySets, Script, Stylesheet

component = Component(
    Script(url="https://example.com/component.js", sri="sha384-js-sri-here"),
    Stylesheet(url="https://example.com/component.css", sri="sha384-css-sri-here"),
)

# conditional components
hijack = Component(
    Script(url="https://example.com/hijack.js" if settings.ENABLE_HIJACK else ""),
    Stylesheet(url="https://example.com/hijack.css" if settings.ENABLE_HIJACK else ""),
)

# local static resources
lib_common = Component(
    Script(url="lib/common.js" if settings.DEBUG else "lib/common.min.js", static=True),
    Stylesheet(
        url="lib/common.css" if settings.DEBUG else "lib/common.min.css", static=True
    ),
)

# Named, ordered dependency sets.
# This dictionary is the value of settings.CLIENT_SIDE_DEPENDENCIES
DEPENDENCIES = DependencySets(
    core=(component, hijack, lib_common),
)
