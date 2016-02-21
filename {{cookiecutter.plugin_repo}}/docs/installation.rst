Installation
------------

 * `Install NodeConductor <http://nodeconductor.readthedocs.org/en/latest/guide/intro.html#installation-from-source>`_
 * Clone NodeConductor {{ cookiecutter.plugin_name }} repository

  .. code-block:: bash

    git clone https://github.com/{{ cookiecutter.organization_name.lower().replace(' ', '') }}/{{ cookiecutter.plugin_repo }}.git

 * Install NodeConductor {{ cookiecutter.plugin_name }} into NodeConductor virtual environment

  .. code-block:: bash

    cd /path/to/{{ cookiecutter.plugin_repo }}/
    python setup.py install

