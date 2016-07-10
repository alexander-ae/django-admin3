#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
setup(
    name = "django-admin-3",
    version = "0.1",
    description = "Administrador de contenidos para django centrado en la personalización",

    packages = find_packages(),

    author = "",
    author_email = "",
    license = "GNU GPL v3",
    keywords = "django,admin",
    url = "https://github.com/alexander-ae/django-admin3",

    install_requires = ['django>=1.8'],
)