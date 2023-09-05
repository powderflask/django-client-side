"""
Hydronet client-side CSS / JS dependency component
See: https://github.com/powderflask/django-client-side

Definition of a client-side dependency:
    a tag, a component with zero or more tags, and a set with zero or more components
"""
from django.template.loader import render_to_string
from django.utils.functional import cached_property


class HtmlTag:
    """Abstract tag used to render a client-side dependency"""

    template = None  # concrete tags must define

    def __init__(self, url, **context):
        """depdendency url and tag template context, eg., sri, static, etc."""
        self.context = {"url": url, **context}

    @cached_property
    def as_string(self):
        return render_to_string(self.template, context=self.context)


class Script(HtmlTag):
    """A script tag"""

    template = "client_side/script.html"


class Stylesheet(HtmlTag):
    """A ling tag"""

    template = "client_side/link.html"


class Component:
    """A set of tags representing single dependency"""

    def __init__(self, *tags):
        self.tags = tags

    def render(self, tag_type):
        return "".join(tag.as_string for tag in self.tags if isinstance(tag, tag_type))


class DependencySets:
    """A set of Components that form a logical client-side application group"""

    def __init__(self, **component_groups):
        """Each component_group is an ordered sequence of Components"""
        self.component_groups = component_groups

    def render(self, group, tag_type):
        """Render the tags of given type for a specific group of components"""
        return "".join(
            component.render(tag_type) for component in self.component_groups[group]
        )
