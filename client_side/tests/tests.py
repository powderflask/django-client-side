from importlib import reload
from django.core import exceptions
from django.test.utils import override_settings
from django.test import TestCase
from client_side.templatetags import dependency_tags
from client_side.tests import dependencies

class TestGetDependencySets(TestCase):

    @override_settings(CLIENT_SIDE_DEPENDENCIES='client_side.tests.dependencies.DEPENDENCIES')
    def test_dotted_path(self):
        dep = dependency_tags.get_dependency_sets()
        self.assertEqual(dep, dependencies.DEPENDENCIES)

    @override_settings(CLIENT_SIDE_DEPENDENCIES={'key': 'value'})
    def test_dictionary(self):
        dep = dependency_tags.get_dependency_sets()
        self.assertEqual(dep, {'key': 'value'})

    @override_settings(CLIENT_SIDE_DEPENDENCIES='dependencies')
    def test_improperly_configured(self):
        self.assertRaises(exceptions.ImproperlyConfigured, dependency_tags.get_dependency_sets)


@override_settings(DEBUG=False)
class TestTemplateTags(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        reload(dependency_tags)

    def test_stylesheet_tag(self):
        links = dependency_tags.stylesheet('core')
        self.assertIn('https://example.com/component.css', links)
        self.assertIn('sha384-css-sri-here', links)
        self.assertIn('lib/common.min.css', links)
        self.assertNotIn('https://example.com/hijack.css', links)

    def test_javascript_tag(self):
        scripts = dependency_tags.javascript('core')
        self.assertIn('https://example.com/component.js', scripts)
        self.assertIn('sha384-js-sri-here', scripts)
        self.assertIn('lib/common.min.js', scripts)
        self.assertNotIn('https://example.com/hijack.js', scripts)


    def test_ie_conditional_shims(self):
        scripts = dependency_tags.javascript('shims')
        self.assertIn('<!--[if lt IE 9]>', scripts)
        self.assertIn('https://somecdn.com/html5shiv.min.js', scripts)
        self.assertIn('<![endif]-->', scripts)


@override_settings(DEBUG=True)
class TestDebugDependencies(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        reload(dependency_tags)

    def test_stylesheet_tag(self):
        links = dependency_tags.stylesheet('core')
        self.assertIn('lib/common.css', links)

    def test_javascript_tag(self):
        scripts = dependency_tags.javascript('core')
        self.assertIn('lib/common.js', scripts)


@override_settings(ENABLE_HIJACK=True)
class TestConditionalDependencies(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        reload(dependency_tags)

    def test_stylesheet_tag(self):
        links = dependency_tags.stylesheet('core')
        self.assertIn('https://example.com/hijack.css', links)

    def test_javascript_tag(self):
        scripts = dependency_tags.javascript('core')
        self.assertIn('https://example.com/hijack.js', scripts)
