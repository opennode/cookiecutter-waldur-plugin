#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    'waldur-core>={{ cookiecutter.waldur_version }}',
]


setup(
    name='{{ cookiecutter.plugin_repo }}',
    version='0.1.0.dev0',
    author='{{ cookiecutter.organization_name }} Team',
    author_email='{{ cookiecutter.organization_email }}',
    url='https://waldur.com',
    description='{{ cookiecutter.plugin_short_description }}',
    long_description=open('README.md').read(),
    license='MIT',
    package_dir={'': 'src'},
    packages=find_packages('src', exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    install_requires=install_requires,
    zip_safe=False,
    entry_points={
        'waldur_extensions': (
            '{{ cookiecutter.plugin_source }} = {{ cookiecutter.plugin_source }}.extension:{{ cookiecutter.plugin_extension_class }}',
        ),
    },
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
)
