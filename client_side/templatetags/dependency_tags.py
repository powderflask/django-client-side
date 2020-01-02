import copy
import itertools
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django import template
register = template.Library()

TEMPLATES = {
    'script': get_template("client_side/script.html"),
    'link': get_template("client_side/link.html"),
}

CONTEXT_VARS = ('link', 'script', 'ie_condition')

dependencies = copy.deepcopy(settings.CLIENT_SIDE_DEPENDENCIES)
# Update module context with conditional dependencies based on value of a truthy setting
for module in itertools.chain(*dependencies.values()):
    overrides = []
    for key in (k for k in module.keys() if k not in CONTEXT_VARS and getattr(settings, k, False)):
        overrides.append(key)  # don't modify dict here in case it changes size
    for key in overrides:
        module.update(module[key])

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
