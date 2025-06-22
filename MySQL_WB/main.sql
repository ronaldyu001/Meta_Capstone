use LittleLemon;
show tables;


# import leaf tables then verify
select * from customers;
select * from staff;
select * from tables;
select * from deliveries;

select * from courses;
select * from drinks;
select * from starters;
select * from sides;
select * from desserts;

# import parent tables then veify
select * from menus;
select * from bookings;

# import grandparent tables then verify
select * from orders;

# update 'orders' table with delivery_id
UPDATE orders o JOIN deliveries d ON o.order_id = d.order_id
SET o.delivery_id = d.delivery_id;


#
#	Exercise: Create a virtual table to summarize data
#

#	Module 2, Task 1
CREATE VIEW OrdersView AS
SELECT order_id, quantity, cost FROM orders;

SELECT * FROM OrdersView;

#	Module 2, Task 2
SELECT 
	c.customer_id AS CustomerID, 
    CONCAT(c.customer_first_name, ' ', c.customer_last_name) AS FullName,
    o.order_id AS OrderID,
    o.cost AS Cost,
    m.menu_name AS MenuName,
    m.starter AS Starter,
    m.course AS Entree,
    m.side AS Side,
    m.drink AS Drink,
    m.dessert AS Dessert
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN menus m ON o.menu_name = m.menu_name
WHERE Cost > 150
ORDER BY Cost ASC;

#	Module 2, Task 3
SELECT menu_name AS MenuName FROM menus WHERE menu_name = ANY(
	SELECT menu_name from orders GROUP BY menu_name HAVING COUNT(order_id) > 2
);


#
#	Exercise: Create optimized queries to manage and analyze data
#

# Module 2, Task 1
DELIMITER //
CREATE PROCEDURE GetMaxQuantity()
BEGIN
	SELECT MAX(quantity) FROM Orders;
END//
DELIMITER ;

CALL GetMaxQuantity();


# Module 2, Task 2
PREPARE GetOrderDetail FROM
'SELECT order_id, quantity, cost FROM Orders WHERE customer_id = ?';

set @id = '00-090-3491';
EXECUTE GetOrderDetail USING @id;
DEALLOCATE PREPARE GetOrderDetail;


# Module 2, Task 3
DROP PROCEDURE IF EXISTS CancelOrder;

DELIMITER //
CREATE PROCEDURE CancelOrder( IN id INT )
BEGIN
	DELETE FROM Orders WHERE order_id = id;
    SELECT CONCAT('Order ', id, ' is cancelled.') AS Confirmation;
END//
DELIMITER ;

CALL CancelOrder( 5 );


#
#	Exercise: Create SQL queries to check available bookings based on user input
#

# Module 2, Task 1
DELETE FROM bookings WHERE booking_id > 4;

SELECT * FROM bookings;

UPDATE bookings
SET booking_date = '2022-10-10', table_no = 5, customer_id = '00-090-3491'
WHERE booking_id = 1;

UPDATE bookings
SET booking_date = '2022-11-12', table_no = 3, customer_id = '00-352-9063'
WHERE booking_id = 2;

UPDATE bookings
SET booking_date = '2022-10-11', table_no = 2, customer_id = '00-381-6823'
WHERE booking_id = 3;

UPDATE bookings
SET booking_date = '2022-10-13', table_no = 2, customer_id = '00-090-3491'
WHERE booking_id = 4;


# Module 2, Task 2
DROP PROCEDURE IF EXISTS CheckBooking;

DELIMITER //
CREATE PROCEDURE CheckBooking( IN b_date DATE, IN tbl_no INT, OUT booking_exists BOOLEAN )
BEGIN
	SET booking_exists = FALSE;
    
    SELECT EXISTS(
		SELECT TRUE FROM bookings
		WHERE booking_date = b_date AND table_no = tbl_no)
	INTO booking_exists;
    
	IF booking_exists THEN 
		SELECT CONCAT('Table ', tbl_no, ' is already booked.') AS 'Booking status';
    END IF;
END//
DELIMITER ;

CALL CheckBooking('2022-11-12', 3);


# Module 2, Task 3
DROP PROCEDURE IF EXISTS AddValidBooking;

DELIMITER //
CREATE PROCEDURE AddValidBooking( IN b_date DATE, IN tbl_no INT )
BEGIN
	DECLARE booking_exists BOOLEAN;
    CALL CheckBooking(b_date, tbl_no, booking_exists);
    
	START TRANSACTION;
		INSERT INTO bookings (booking_id, booking_date, table_no)
        SELECT MAX(booking_id) + 1, b_date, tbl_no FROM bookings;
    
    IF booking_exists THEN
		ROLLBACK;
        SELECT CONCAT('Table ', tbl_no, ' is already booked - booking cancelled') AS 'Booking status';
	ELSE COMMIT;
    END IF;
END//
DELIMITER ;

CALL AddValidBooking('2022-10-10', 5);


#
#	Exercise: Create SQL queries to add and update bookings
# 

# Module 2, Task 1
DROP PROCEDURE IF EXISTS AddBooking;

DELIMITER //
CREATE PROCEDURE AddBooking ( IN b_id INT, IN c_id VARCHAR(100), IN b_date DATE, IN tbl_no INT )
BEGIN
	INSERT INTO bookings (booking_id, customer_id, booking_date, table_no)
    VALUES(b_id, c_id, b_date, tbl_no);
    SELECT CONCAT('New booking added;') AS Confirmation;
END//
DELIMITER ;

CALL AddBooking(9, '00-090-3491', '2022-12-30', 4);

DELETE FROM Bookings WHERE booking_id = 9;
SELECT * FROM bookings;


# Module 2, Task 2
DROP PROCEDURE IF EXISTS UpdateBooking;

DELIMITER //
CREATE PROCEDURE UpdateBooking( IN b_id INT, IN b_date DATE )
BEGIN
	UPDATE bookings SET booking_date = b_date WHERE booking_id = b_id;
    SELECT CONCAT('Booking ', b_id, ' updated.') AS Confirmation;
END//
DELIMITER ;

CALL UpdateBooking(9, '2022-12-17');

select * from bookings;


# Module 2, Task 3
DROP PROCEDURE IF EXISTS CancelBooking;

DELIMITER //
CREATE PROCEDURE CancelBooking( IN b_id INT )
BEGIN
	DELETE FROM Bookings WHERE booking_id = b_id;
    SELECT CONCAT('Booking ', b_id,' cancelled.') AS Confirmation;
END//
DELIMITER ;

CALL CancelBooking(9)
