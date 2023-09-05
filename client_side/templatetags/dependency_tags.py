import copy
import importlib

from django import template
from django.conf import settings
from django.core import exceptions
from django.utils.safestring import mark_safe

from client_side.component import Script, Stylesheet

register = template.Library()


def get_dependency_sets(client_side_dependencies=None):
    """return the client-side dependencies dict from a dotted path or a dictionary object"""
    dependencies_obj = client_side_dependencies or settings.CLIENT_SIDE_DEPENDENCIES
    # Allow for dependencies defined directly
    if type(dependencies_obj) is dict:
        return dependencies_obj
    # Allow for relative paths
    dependencies_path = dependencies_obj.split(".")
    dependencies_dict = dependencies_path[-1]
    if len(dependencies_path) > 1:
        dependencies_module_name = ".".join(dependencies_path[:-1])
    else:
        raise exceptions.ImproperlyConfigured(
            "settings.CLIENT_SIDE_DEPENDENCIES must be a dotted-path or a dict."
        )
    dependencies_module = importlib.import_module(dependencies_module_name)
    return getattr(dependencies_module, dependencies_dict)


dependency_sets = copy.deepcopy(get_dependency_sets())


@register.simple_tag
def javascript(group):
    return mark_safe(dependency_sets.render(group, Script))


@register.simple_tag
def stylesheet(group):
    return mark_safe(dependency_sets.render(group, Stylesheet))
