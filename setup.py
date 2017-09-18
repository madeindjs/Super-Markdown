#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import SuperMarkdown

setup(

    name='SuperMarkdown',

    version="0.2.4",
    packages=find_packages(),

    author="Rousseau Alexandre",
    author_email="rousseaualexandre.lyon@gmail.com",

    description="export a complex Markdown file into a standalone HTML file.",
    long_description=open('README.md').read(),

    install_requires=['Markdown','markdown-checklist','graphviz','beautifulsoup4'],


    include_package_data=True,
    eager_resources={'':[
        'snippet.html',
        ]},


    url='https://github.com/madeindjs/Super-Markdown',


    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Programming Language :: Python :: 3.4",
        "Topic :: Communications",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Markup :: HTML",

    ],


    entry_points = {
        'console_scripts': [
            'super-markdown = SuperMarkdown.SuperMarkdown:main',
        ],
    },


)
