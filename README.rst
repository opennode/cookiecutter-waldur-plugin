Usage
=====

In order to create proper plugin repository structure, please execute following steps:

1. `Install cookiecutter <http://cookiecutter.readthedocs.org/en/latest/installation.html>`_

2. Install Waldur plugin for cookiecutter:

  .. code-block:: bash

    cookiecutter https://github.com/opennode/cookiecutter-waldur-plugin.git


You will be prompted to enter values of some variables.
Note, that in brackets will be suggested default values.

- plugin_name - name of the plugin. i.e. `SugarCRM`
- plugin_repo - name of the plugin's repository. i.e. `waldur-sugarcrm`
- plugin_source - name of the directory inside **src** folder. i.e. `waldur_sugarcrm`
- plugin_extension_class - name of the class inside **extension.py** file i.e. `SugarCRMExtension`
- plugin_app_config_class - name of the class inside **apps.py** file i.e. `SugarCRMConfig`
- plugin_short_description - short description of the plugin
- waldur_version - version of the `Waldur <http://docs.waldur.com/>`_
  application this plugin depends on. i.e. `0.151.0`
- year - current year i.e. `2017`
- organization - name of the organization i.e. `OpenNode`
- github_username - GitHub username i.e. `opennode`


Implementing services
=====================

Usually Waldur plugin implements service, for example for OpenStack or Zabbix.
Service consists of backend class, database models and API views. Service catalog maintains metadata about all connected services.

In order to specify ID of service settings in the database, add the following property to the application configuration class in `apps.py` file.
Note that once `service_name` is set up, it should not be modified without migration.

.. code-block:: python

    service_name = '{{ cookiecutter.plugin_name }}'


It is assumed that service backend is implemented in **backend.py** file.
In order to connect backend class to the service catalog, add the following code to `ready` method of the application configuration class.
When service backend is connected, related database models are connected as well.

.. code-block:: python

    from waldur_core.structure import SupportedServices
    from .backend import Backend
    SupportedServices.register_backend(Backend)

Adding new URLs
===============

If Waldur plugin adds a new Django URL, it should be registered in `urls.py` file:

.. code-block:: python

    urlpatterns = [
        url(r'^my/new/url/', views.page),
    ]

See also: https://docs.djangoproject.com/en/1.11/topics/http/urls/#url-dispatcher

For Django to be able to use these URL configurations make sure this method exists in `extension.py` or add it:

.. code-block:: python

    @staticmethod
    def django_urls():
        from .urls import urlpatterns
        return urlpatterns
