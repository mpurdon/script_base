#!/usr/bin/env python

import io
import re

from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()

setup(
    name='{{ cookiecutter.distribution_name }}',
    version='{{ cookiecutter.version }}',
    license='{{ cookiecutter.license }}',
    description={{ '{0!r}'.format(cookiecutter.project_short_description).lstrip('ub') }},
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author={{ '{0!r}'.format(cookiecutter.full_name).lstrip('ub') }},
    author_email={{ '{0!r}'.format(cookiecutter.email).lstrip('ub') }},
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
{%- if cookiecutter.license in ["BSD 2-Clause License", "BSD 3-Clause License"] %}
        'License :: OSI Approved :: BSD License',
{%- elif cookiecutter.license == "MIT license" %}
        'License :: OSI Approved :: MIT License',
{%- elif cookiecutter.license == "Public Domain" %}
        'License :: Public Domain',
{%- endif %}

        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
    project_urls={
{%- if cookiecutter.sphinx_docs == "yes" %}
        'Documentation': 'https://{{ cookiecutter.repo_name|replace('.', '') }}.readthedocs.io/',
        'Changelog': 'https://{{ cookiecutter.repo_name|replace('.', '') }}.readthedocs.io/en/latest/changelog.html',
{%- else %}
        'Changelog': 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/blob/master/CHANGELOG.rst',
{%- endif %}
        'Issue Tracker': 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues',
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires=['>=3.6',],
    install_requires=[
{%- if cookiecutter.command_line_interface == 'click' %}
        'click',
{%- endif %}
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
{%- if cookiecutter.command_line_interface != 'no' %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.command_line_interface_bin_name }} = {{ cookiecutter.package_name }}.cli:main',
        ]
    },
{%- endif %}
)
