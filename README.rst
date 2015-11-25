Usage
=====

In order to create proper plugin repository structure, please execute following steps:

1. `Install cookiecutter <http://cookiecutter.readthedocs.org/en/latest/installation.html>`_

2. Install NodeConductor plugin cookiecutter:

  .. code-block:: bash

    cookiecutter https://github.com/opennode/cookiecutter-nodeconductor-plugin.git


You will be prompted to enter values of some variables.
Note, that in brackets will be suggested default values.

- plugin_name - name of the plugin.
  **Important! It should start with word NodeConductor** i.e. `NodeConductor SugarCRM`
- plugin_repo - name of the plugin's repository. i.e. `nodeconductor-sugarcrm`
- plugin_source - name of the directory inside **src** folder. i.e. `nodeconductor_sugarcrm`
- plugin_extension_class - name of the class inside **extension.py** file i.e. `SugarCRMExtension`
- plugin_short_description - short description of the plugin
- nodeconductor_version - version of the `NodeConductor <http://nodeconductor.readthedocs.org/en/stable/index.html>`_
  application this plugin depends on. i.e. `0.81.0`
- year - current year i.e. `2015`

