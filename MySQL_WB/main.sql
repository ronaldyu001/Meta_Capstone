use LittleLemon;
show tables;

select * from Orders;
select * from Menus;
select * from Bookings;
select * from Customers;


# Customers
INSERT INTO Customers (GuestFirstName, GuestLastName)
SELECT DISTINCT GuestFirstName, GuestLastName FROM Bookings;

# Update Bookings CustomerIDs
UPDATE Bookings b
JOIN Customers  c
ON b.GuestFirstName = c.GuestFirstName
AND b.GuestLastName = c.GuestLastName
SET b.CustomerID = c.CustomerID;

ALTER TABLE Bookings 
DROP COLUMN GuestFirstName, 
DROP COLUMN GuestLastName;

# Module 2, Task 1
CREATE VIEW OrdersView AS
SELECT OrderID, Quantity, BillAmount FROM Orders;
select * from OrdersView;

# Module 2, Task 2
select 
	o.CustomerID, 
    CONCAT(c.GuestFirstName, ' ', c.GuestLastName), 
    OrderID, 
    BillAmount AS Cost, 
    Cuisine AS MenuName, 
    Name AS CourseName
FROM Orders AS o 
LEFT JOIN Menus AS m ON o.MenuID = m.MenuID
LEFT JOIN MenuItems as mi ON m.ItemID = mi.ItemID
LEFT JOIN Customers as c ON o.CustomerID = 