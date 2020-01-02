import sys, os

from setuptools import setup, Command
from setuptools.command.test import test

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./*.pyc ./*.egg-info')


def run_tests(*args):
    from client_side.tests import run_tests
    errors = run_tests()
    if errors:
        sys.exit(1)
    else:
        sys.exit(0)


test.run_tests = run_tests

LONG_DESCRIPTION = """
==================
django-client-side
==================

Simple client-side dependency management for your django project.
Keep and update client-side dependencies in one place (e.g., not scattered in templates).
Template tags used to pull client-side dependencies into templates.
Use any client-side framework or none.  Demo app uses npm as JS package manager and build tool.
"""

setup(
    name='django-client-side',
    version='0.1.0',
    packages=['client_side', ],
    license='MIT',
    include_package_data = True,
    description='Simple client-side dependency management for your django project.',
    long_description=LONG_DESCRIPTION,
    author='powderflask',
    author_email='powderflask@gmail.com',
    maintainer='powderflask',
    maintainer_email='powderflask@gmail.com',
    url='https://github.com/powderflask/django-client-side',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
    cmdclass={
        'clean' : CleanCommand,
    },
    test_suite='dummy',
)

