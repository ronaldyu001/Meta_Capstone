import db_funcs.create_db as create_db


"""
Set up the LittleLemon database.
"""
# connect (login credentials manually set)
connection = create_db.connect()

# create database
create_db.create_db( connection )
# create tables (this will drop the existing tables)
create_db.create_tables( connection )
# populate tables
create_db.populate_tables( connection )

