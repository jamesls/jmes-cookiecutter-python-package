#!/usr/bin/env python
from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    README = readme_file.read()


install_requires = [
    # Package requirements go here.
]


setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description="{{ cookiecutter.project_short_description }}",
    long_description=README,
    author="{{ cookiecutter.full_name }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    license="Apache License 2.0",
    zip_safe=False,
    keywords='{{ cookiecutter.project_slug }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
