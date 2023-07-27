-- 5.1
ALTER TABLE student 
ADD COLUMN email VARCHAR(30) UNIQUE;
-- 
ALTER TABLE student RENAME COLUMN full_name
TO name;

-- 
ALTER TABLE student RENAME TO students;
-- 
ALTER TABLE students RENAME COLUMN major TO field;
-- 
ALTER TABLE students  ALTER COLUMN field SET NOT NULL;
ALTER TABLE students  ALTER COLUMN university SET NOT NULL;


-- 
ALTER TABLE people ADD COLUMN phone BIGINT UNIQUE;

ALTER TABLE people RENAME COLUMN first_name TO given_name;

ALTER TABLE people ALTER COLUMN is_married SET DEFAULT false;

-- 
ALTER TABLE products ADD COLUMN description text;

ALTER TABLE products ALTER COLUMN expiration_date TYPE TIMESTAMP;

ALTER TABLE products RENAME COLUMN made_in TO country;

ALTER TABLE products ALTER COLUMN company SET DEFAULT 'Unkown';

-- 
ALTER TABLE films ADD COLUMN language VARCHAR(20);

ALTER TABLE films ALTER COLUMN duration TYPE INT;

ALTER TABLE films RENAME COLUMN rate TO rating;

ALTER TABLE films ALTER COLUMN country SET DEFAULT 'Unkown';


-- 
ALTER TABLE customer ADD COLUMN phone BIGINT UNIQUE;

ALTER TABLE customer RENAME COLUMN address TO shipping_to;

ALTER TABLE customer ALTER COLUMN name SET NOT NULL;

-- 
ALTER TABLE order ADD COLUMN customer_id INT UNIQUE;

ALTER TABLE order ALTER COLUMN price TYPE MONEY;

ALTER TABLE order ALTER COLUMN order_date SET DEFAULT now();
