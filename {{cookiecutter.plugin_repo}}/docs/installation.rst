Installation
------------

* `Install Waldur Core <https://github.com/opennode/waldur-core/blob/develop/docs/guide/install-from-src.rst>`_

* Clone Waldur {{ cookiecutter.plugin_name }} repository

  .. code-block:: bash

    git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.plugin_repo }}.git

* Install Waldur {{ cookiecutter.plugin_name }} into Waldur virtual environment

  .. code-block:: bash

    cd /path/to/{{ cookiecutter.plugin_repo }}/
    python setup.py install
