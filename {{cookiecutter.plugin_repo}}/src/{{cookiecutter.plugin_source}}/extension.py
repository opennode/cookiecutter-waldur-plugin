from __future__ import unicode_literals

from nodeconductor.core import NodeConductorExtension


class {{ cookiecutter.plugin_extension_class }}(NodeConductorExtension):

    @staticmethod
    def django_app():
        return '{{ cookiecutter.plugin_source }}'

    @staticmethod
    def rest_urls():
        from .urls import register_in
        return register_in

