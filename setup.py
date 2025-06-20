from __future__ import print_function # TODO: This can probably be removed in the future
from setuptools import setup

import sys
import unittest


def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('pony.orm.tests', pattern='test_*.py')
    return test_suite


name: str = "pony"

version: str = __import__('pony').__version__

description: str = "Pony Object-Relational Mapper"

long_description: str = """
    About
    =====
    Pony ORM is easy to use and powerful object-relational mapper for Python.
    Using Pony, developers can create and maintain database-oriented software applications
    faster and with less effort. One of the most interesting features of Pony is
    its ability to write queries to the database using generator expressions.
    Pony then analyzes the abstract syntax tree of a generator and translates it
    to its SQL equivalent.

    Following is an example of a query in Pony::
        select(p for p in Product if p.name.startswith('A') and p.cost <= 1000)

    Such approach simplify the code and allows a programmer to concentrate
    on the business logic of the application.

    Pony translates queries to SQL using a specific database dialect.
    Currently Pony works with SQLite, MySQL, PostgreSQL and Oracle databases.

    The package `pony.orm.examples <https://github.com/ponyorm/pony/tree/orm/pony/orm/examples>`_
    contains several examples.

    
    Installation
    ============
    ::

    pip install pony

    
    Entity-Relationship Diagram Editor
    ==================================
    `Pony online ER Diagram Editor <https://editor.ponyorm.com>`_ is a great tool for prototyping.
    You can draw your ER diagram online, generate  Pony entity declarations or SQL script for
    creating database schema based on the diagram and start working with the database in seconds.

    
    Pony ORM Links:
    =================
    - Main site: https://ponyorm.com
    - Documentation: https://docs.ponyorm.com
    - GitHub: https://github.com/ponyorm/pony
    - Mailing list:  http://ponyorm-list.ponyorm.com
    - ER Diagram Editor: https://editor.ponyorm.com
    - Blog: https://blog.ponyorm.com
"""
classifiers: list[str] = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development :: Libraries',
    'Topic :: Database'
]

author: str = ', '.join([
    'Alexander Kozlovsky <alexander.kozlovsky@gmail.com>'
    , 'Alexey Malashkevich <alexey@ponyorm.org>'
    , 'Alexander Tischenko <sashaaero@yandex.ru>'
])

author_email: str = "team@ponyorm.com"

url: str = "https://ponyorm.com"

project_urls: dict[str, str] = {
    "Documentation": "https://docs.ponyorm.org",
    "Source": "https://github.com/ponyorm/pony",
}

licence: str = "Apache License Version 2.0"

packages: list[str] = [
    "pony",
    "pony.flask",
    #"pony.flask.example",
    "pony.orm",
    "pony.orm.dbproviders",
    #"pony.orm.examples",
    "pony.orm.integration",
    "pony.orm.tests",
    "pony.thirdparty",
    "pony.utils"
]

package_data: dict[str, list[str]] = {
    'pony.flask.example': ['templates/*.html'],
    'pony.orm.tests': ['queries.txt']
}

download_url: str = "http://pypi.python.org/pypi/pony/"


if __name__ == "__main__":
    pv: tuple[int, int] = sys.version_info[:2]
    
    if pv < (3, 8) or pv > (3, 12):
        s = "Sorry, but %s %s requires Python of one of the following versions: 3.8-3.12." \
            " You have version %s"
        print(s % (name, version, sys.version.split(' ', 1)[0]))
        sys.exit(1)

    setup(
        name=name,
        version=version,
        description=description,
        long_description=long_description,
        classifiers=classifiers,
        author=author,
        author_email=author_email,
        url=url,
        project_urls=project_urls,
        license=licence,
        packages=packages,
        package_data=package_data,
        download_url=download_url,
        test_suite='setup.test_suite'
    )
