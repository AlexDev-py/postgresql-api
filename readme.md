# PostgreSQL API [![Downloads](https://pepy.tech/badge/postgresql-api)](https://pepy.tech/project/postgresql-api) [![PyPi version](https://img.shields.io/pypi/v/postgresql-api.svg)](https://pypi.python.org/pypi/postgresql-api/) [![](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/AlexDev-py/postgresql_api/blob/2.0.0/LICENSE)

Installation
------------

Install from [PyPi](https://pypi.org/project/postgresql-api)

    pip install postgresql-api


Install from [GitHub](https://github.com/AlexDev-py/postgresql_api.git)

    git clone https://github.com/AlexDev-py/postgresql_api.git

Create table classes
--------------------

    from sqlite3_api.Table import Table

    class MyTable(Table):
        my_first_field: str
        my_second_field: int

In file 
[example/my_tables.py](https://github.com/AlexDev-py/sqlite3_api/blob/2.0.0/example/my_tables.py),
there is an instruction to create classes(in Russian language)

Using
------------

Initiate the database:

    from my_tables import MyTable 
    my_table = MyTable('MyDataBase.sqlite')

Create tables:

    my_table.create_table()

Inserting data:

    my_table.insert(
        my_first_field='first',
        my_second_field='second',
    )

Getting data:

    data = my_table.filter()

Sorting data:

    data = my_table.filter(my_field='value')


More information in the 
[example folder](https://github.com/AlexDev-py/sqlite3_api/tree/2.0.0/example)

VK: [AlexDev](https://vk.com/sys.exit1)