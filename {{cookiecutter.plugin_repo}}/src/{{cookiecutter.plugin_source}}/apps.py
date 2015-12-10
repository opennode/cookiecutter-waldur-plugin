from django.apps import AppConfig


class {{ cookiecutter.plugin_app_config_class }}(AppConfig):
    name = '{{ cookiecutter.plugin_source }}'
    verbose_name = '{{ cookiecutter.plugin_name }}'

    def ready(self):
        pass
