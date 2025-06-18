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


# import mysql connector
import mysql.connector as connector
from mysql.connector import Error
from mysql.connector import pooling



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


def create_cursor( connection ):
    # create cursor
    try:
        cursor = connection.cursor()
        print(f'Cursor for "ronald" created.\n')
    except Error as Err:
        raise Err(f'Could not create cursor:\nError Number: {Err.errno}\nError Message: {Err.errmsg}\n')
    
    return cursor



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

    # drop tables if already exists
    cursor.execute("DROP TABLE IF EXISTS MenuItems;")
    cursor.execute("DROP TABLE IF EXISTS Menus;")
    cursor.execute("DROP TABLE IF EXISTS Bookings;")
    cursor.execute("DROP TABLE IF EXISTS Orders;")
    cursor.execute("DROP TABLE IF EXISTS Employees;")

    # MenuItems table
    create_menuitem_table = """CREATE TABLE IF NOT EXISTS MenuItems (
    ItemID INT AUTO_INCREMENT,
    Name VARCHAR(200),
    Type VARCHAR(100),
    Price INT,
    PRIMARY KEY (ItemID)
    );"""

    # Menus table
    create_menu_table = """CREATE TABLE IF NOT EXISTS Menus (
    MenuID INT,
    ItemID INT,
    Cuisine VARCHAR(100),
    PRIMARY KEY (MenuID,ItemID)
    );"""

    # Bookings table
    create_booking_table = """CREATE TABLE IF NOT EXISTS Bookings (
    BookingID INT AUTO_INCREMENT,
    TableNo INT,
    GuestFirstName VARCHAR(100) NOT NULL,
    GuestLastName VARCHAR(100) NOT NULL,
    BookingSlot TIME NOT NULL,
    EmployeeID INT,
    PRIMARY KEY (BookingID)
    );"""

    # Orders table
    create_orders_table = """CREATE TABLE IF NOT EXISTS Orders (
    OrderID INT,
    TableNo INT,
    MenuID INT,
    BookingID INT,
    BillAmount INT,
    Quantity INT,
    PRIMARY KEY (OrderID,TableNo)
    );"""

    # Employees table
    create_employees_table = """CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR (255),
    Role VARCHAR (100),
    Address VARCHAR (255),
    Contact_Number INT,
    Email VARCHAR (255),
    Annual_Salary VARCHAR (100)
    );"""

    # Create MenuItems table
    cursor.execute(create_menuitem_table)
    print(f'MenuItems table created.')

    # Create Menu table
    cursor.execute(create_menu_table)
    print(f'Menus table created.')

    # Create Bookings table
    cursor.execute(create_booking_table)
    print(f'Bookings table created.')

    # Create Orders table
    cursor.execute(create_orders_table)
    print(f'Orders table created.')

    # Create Employees table
    cursor.execute(create_employees_table)
    print(f'Employees table created.')

    print(f'\nMSG: All tables created.\n')


def populate_tables( connection ):
    cursor = create_cursor( connection )

    #*******************************************************#
    # Insert query to populate "MenuItems" table:
    #*******************************************************#
    insert_menuitems="""
    INSERT INTO MenuItems (ItemID, Name, Type, Price)
    VALUES
    (1, 'Olives','Starters',5),
    (2, 'Flatbread','Starters', 5),
    (3, 'Minestrone', 'Starters', 8),
    (4, 'Tomato bread','Starters', 8),
    (5, 'Falafel', 'Starters', 7),
    (6, 'Hummus', 'Starters', 5),
    (7, 'Greek salad', 'Main Courses', 15),
    (8, 'Bean soup', 'Main Courses', 12),
    (9, 'Pizza', 'Main Courses', 15),
    (10, 'Greek yoghurt','Desserts', 7),
    (11, 'Ice cream', 'Desserts', 6),
    (12, 'Cheesecake', 'Desserts', 4),
    (13, 'Athens White wine', 'Drinks', 25),
    (14, 'Corfu Red Wine', 'Drinks', 30),
    (15, 'Turkish Coffee', 'Drinks', 10),
    (16, 'Turkish Coffee', 'Drinks', 10),
    (17, 'Kabasa', 'Main Courses', 17);"""

    #*******************************************************#
    # Insert query to populate "Menu" table:
    #*******************************************************#
    insert_menu="""
    INSERT INTO Menus (MenuID,ItemID,Cuisine)
    VALUES
    (1, 1, 'Greek'),
    (1, 7, 'Greek'),
    (1, 10, 'Greek'),
    (1, 13, 'Greek'),
    (2, 3, 'Italian'),
    (2, 9, 'Italian'),
    (2, 12, 'Italian'),
    (2, 15, 'Italian'),
    (3, 5, 'Turkish'),
    (3, 17, 'Turkish'),
    (3, 11, 'Turkish'),
    (3, 16, 'Turkish');"""

    #*******************************************************#
    # Insert query to populate "Bookings" table:
    #*******************************************************#
    insert_bookings="""
    INSERT INTO Bookings (BookingID, TableNo, GuestFirstName, 
    GuestLastName, BookingSlot, EmployeeID)
    VALUES
    (1, 12, 'Anna','Iversen','19:00:00',1),
    (2, 12, 'Joakim', 'Iversen', '19:00:00', 1),
    (3, 19, 'Vanessa', 'McCarthy', '15:00:00', 3),
    (4, 15, 'Marcos', 'Romero', '17:30:00', 4),
    (5, 5, 'Hiroki', 'Yamane', '18:30:00', 2),
    (6, 8, 'Diana', 'Pinto', '20:00:00', 5);"""

    #*******************************************************#
    # Insert query to populate "Orders" table:
    #*******************************************************#
    insert_orders="""
    INSERT INTO Orders (OrderID, TableNo, MenuID, BookingID, Quantity, BillAmount)
    VALUES
    (1, 12, 1, 1, 2, 86),
    (2, 19, 2, 2, 1, 37),
    (3, 15, 2, 3, 1, 37),
    (4, 5, 3, 4, 1, 40),
    (5, 8, 1, 5, 1, 43);"""

    #*******************************************************#
    # Insert query to populate "Employees" table:
    #*******************************************************#
    insert_employees = """
    INSERT INTO employees (EmployeeID, Name, Role, Address, Contact_Number, Email, Annual_Salary) VALUES
    (01,'Mario Gollini','Manager','724, Parsley Lane, Old Town, Chicago, IL',351258074,'Mario.g@littlelemon.com','$70,000'),
    (02,'Adrian Gollini','Assistant Manager','334, Dill Square, Lincoln Park, Chicago, IL',351474048,'Adrian.g@littlelemon.com','$65,000'),
    (03,'Giorgos Dioudis','Head Chef','879 Sage Street, West Loop, Chicago, IL',351970582,'Giorgos.d@littlelemon.com','$50,000'),
    (04,'Fatma Kaya','Assistant Chef','132  Bay Lane, Chicago, IL',351963569,'Fatma.k@littlelemon.com','$45,000'),
    (05,'Elena Salvai','Head Waiter','989 Thyme Square, EdgeWater, Chicago, IL',351074198,'Elena.s@littlelemon.com','$40,000'),
    (06,'John Millar','Receptionist','245 Dill Square, Lincoln Park, Chicago, IL',351584508,'John.m@littlelemon.com','$35,000');"""

    # Populate MenuItems table
    cursor.execute(insert_menuitems)
    connection.commit()
    print(f'MenuItems table populated.')

    # Populate MenuItems table
    cursor.execute(insert_menu)
    connection.commit()
    print(f'Menus table populated.')


    # Populate Bookings table
    cursor.execute(insert_bookings)
    connection.commit()
    print(f'Bookings table populated.')


    # Populate Orders table
    cursor.execute(insert_orders)
    connection.commit()
    print(f'Orders table populated.')


    # Populate Employees table
    cursor.execute(insert_employees)
    connection.commit()
    print(f'Employees table populated.')


    print(f'\nMSG: All tables poppulated.\n')