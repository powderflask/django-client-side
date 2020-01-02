import importlib
import copy
import itertools
from django.conf import settings
from django.core import exceptions
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django import template
register = template.Library()

TEMPLATES = {
    'script': get_template("client_side/script.html"),
    'link': get_template("client_side/link.html"),
}

CONTEXT_VARS = ('link', 'script', 'ie_condition')


def get_dependency_sets(client_side_dependencies=None):
    """ return the client-side dependencies dict from a dotted path or a dictionary object """
    dependencies_obj = client_side_dependencies or settings.CLIENT_SIDE_DEPENDENCIES
    # Allow for dependencies defined directly
    if type(dependencies_obj) is dict:
        return dependencies_obj
    # Allow for relative paths
    dependencies_path = dependencies_obj.split('.')
    dependencies_dict = dependencies_path[-1]
    if len(dependencies_path) > 1:
        dependencies_module_name = '.'.join(dependencies_path[:-1])
    else:
        raise exceptions.ImproperlyConfigured('settings.CLIENT_SIDE_DEPENDENCIES must be a dotted-path or a dict.')
    dependencies_module = importlib.import_module(dependencies_module_name)
    return getattr(dependencies_module, dependencies_dict)


dependencies = copy.deepcopy(get_dependency_sets())

# Update component contexts with conditional dependencies based on value of a truthy setting
for component in itertools.chain(*dependencies.values()):
    overrides = []
    for key in (k for k in component.keys() if k not in CONTEXT_VARS and getattr(settings, k, False)):
        overrides.append(key)  # don't modify dict here in case it changes size
    for key in overrides:
        component.update(component[key])

SCRIPT_TAGS = {
    name: [TEMPLATES['script'].render(context=component) for component in group if 'script' in component.keys()]
    for name, group in dependencies.items()
}

LINK_TAGS = {
    name: [TEMPLATES['link'].render(context=component) for component in group if 'link' in component.keys()]
    for name, group in dependencies.items()
}


@register.simple_tag
def javascript(name):
    return mark_safe(''.join(SCRIPT_TAGS[name]))


@register.simple_tag
def stylesheet(name):
    return mark_safe(''.join(LINK_TAGS[name]))
