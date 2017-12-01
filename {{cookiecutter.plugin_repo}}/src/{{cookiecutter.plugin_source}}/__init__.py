from waldur_core import _get_version

__version__ = _get_version('{{ cookiecutter.plugin_source }}')

default_app_config = '{{ cookiecutter.plugin_source }}.apps.{{ cookiecutter.plugin_app_config_class }}'
