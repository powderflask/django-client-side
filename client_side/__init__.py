""""
django-client-side.

Simple client-side dependency management
"""
import django

__version__ = "0.2.0"
__author__ = "powderflask"
if django.VERSION < (3, 2):
    default_app_config = "client_side.apps.ClientSideConfig"
