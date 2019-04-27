# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os import path
from io import open
from re import search, M

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Get the version from the slackclient/version.py file
with open(path.join(here, "slackclient", "version.py"), encoding="utf-8") as f:
    version_file = f.read()
    version_match = search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string")

setup(
    name="slackclient-remix",
    version=version,
    description="Slack API clients for Web API and RTM API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aoberoi/python-slackclient-remix",
    author="Ankur Oberoi",
    author_email="aoberoi@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Chat",
        "Topic :: System :: Networking",
        "Topic :: Office/Business",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="slack slack-web slack-rtm chat chatbots bots chatops",
    project_urls={
        "Documentation": "https://github.com/aoberoi/python-slackclient-remix",
        "Say Thanks!": "https://saythanks.io/to/aoberoi",
        "Source": "https://github.com/aoberoi/python-slackclient-remix",
        "Tracker": "https://github.com/aoberoi/python-slackclient-remix/issues",
        "Coverage": "https://codecov.io/gh/aoberoi/python-slackclient-remix",
        "Build Status": "https://travis-ci.com/aoberoi/python-slackclient-remix",
        "Build Status (Windows)": "https://ci.appveyor.com/project/aoberoi/python-slackclient-remix",
    },
    packages=find_packages(exclude=["docs", "docs-src", "tests"]),
    install_requires=[
        "websocket-client >=0.35, <0.55.0",
        "requests >=2.11, <3.0a0",
        "six >=1.10, <2.0a0",
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4",
)
