import initialize_db


"""
Set up the LittleLemon database.
"""
# connect (login credentials manually set)
connection = initialize_db.connect()
# create database
initialize_db.create_db( connection )
# create tables (this will drop the existing tables)
initialize_db.create_tables( connection )
# populate tables
initialize_db.populate_tables( connection )

