"""
---------------------------------------------------------------
Little Lemon Init:

- Create virtual environment for this project.
- Connect to local mysql server
    - Make sure local mysql server is created.
        - python3 -m venv venv
        - source venv/bin/activate
- Create database
- Create tables
- Insert data into tables

( This code was previously provided for use during the Meta DB Engineering Certificate )
---------------------------------------------------------------
"""


# import
import mysql.connector as connector
from mysql.connector import Error
from mysql.connector import pooling
from utility_funcs import create_cursor


def connect():
    # establish connection
    try:
        connection = connector.connect(
            user="ronald",
            password="MetaCert123"
        )
        print(f'\nUser "ronald" successfully connected.')
    except Error as Err:
        raise Err(f'Could not connect:\nError Number: {Err.errno}\nError Message: {Err.errmsg}\n')
    
    return connection


def create_db( connection ):
    # create cursor
    cursor = create_cursor( connection )

    # create the database
    cursor.execute("DROP DATABASE IF EXISTS LittleLemon;")
    cursor.execute("CREATE DATABASE IF NOT EXISTS LittleLemon;")
    print(f'MSG: LittleLemon database successfuly created.\n\n    Available Databases:')

    cursor.execute("SHOW DATABASES;")
    for row in cursor:
        print(f'        {row[0]}')

    cursor.execute("USE LittleLemon;")
    print(f'\nMSG: LittleLemon database selected for use.\n')

    return connection


def create_tables( connection ):
    cursor = create_cursor( connection )

    
def populate_tables( connection ):
    cursor = create_cursor( connection )
