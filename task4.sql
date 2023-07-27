-- 4.1
SELECT full_name, university, first_name, students.country
FROM students
INNER JOIN people ON students.id = people.id;

-- 
SELECT full_name, country, major, name, made_in, price
FROM students
LEFT JOIN products ON country = made_in,

-- 4.2
CREATE TABLE customer (
id INT NOT NULL,
name VARCHAR(25) NOT NULL,
email VARCHAR(50) NOT NULL,
address VARCHAR(35) NOT NULL);

-- 
CREATE TABLE order1 (
id INT NOT NULL,
name VARCHAR(35) NOT NULL,
order_date DATE NOT NULL,
price INT
);

-- 

SELECT customer.name, email, address, order.name, order_date, price
FROM customer
INNER JOIN order1 ON customer.id = order.id;

