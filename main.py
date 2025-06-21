import db_funcs as db_funcs


"""
Set up the LittleLemon database.
"""
# connect (login credentials manually set)
connection = db_funcs.connect()

# create database
db_funcs.create_db( connection )
