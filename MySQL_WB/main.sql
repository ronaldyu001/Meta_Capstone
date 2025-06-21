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

CALL CancelOrder( 5 )
