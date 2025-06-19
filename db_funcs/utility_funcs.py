# imports
import mysql.connector as connector
from mysql.connector import Error


# create cursor
def create_cursor( connection ):
    # create cursor
    try:
        cursor = connection.cursor()
        print(f'Cursor for "ronald" created.\n')
    except Error as Err:
        raise Err(f'Could not create cursor:\nError Number: {Err.errno}\nError Message: {Err.errmsg}\n')
    
    return cursor