-- Task 1

-- 1.1
CREATE DATABASE Practice;
CREATE DATABASE Homework;


-- practice databasega malumot yuklaydi
\c practice
-- 1.2
CREATE TABLE students (
    id INT NOT NULL UNIQUE,
    full_name VARCHAR(30) NOT NULL,
    country VARCHAR(50) NOT NULL,
    passport VARCHAR(10) NOT NULL UNIQUE,
    university VARCHAR(65) NOT NULL,
    date_of_birth DATE NOT NULL,
    major VARCHAR(30)
);

-- 

CREATE TABLE people (
 id INT NOT NULL UNIQUE,
 last_name VARCHAR(20) NOT NULL,
 first_name VARCHAR(20) NOT NULL,
 passport VARCHAR(9) CHECK (passport ~* '^[A-Za-z0-9]+$'),
 date_of_birth DATE NOT NULL,
 country VARCHAR(40) NOT NULL,
 is_married VARCHAR(5)
);

-- homework databasega o'tadi
\c homework

-- 1.3
CREATE TYPE FRUIT as ENUM ('apple', 'banana', 'orange', 'strawberry', 'pineapple');

CREATE TABLE products (
 id INT NOT NULL UNIQUE,
 name VARCHAR(15) NOT NULL,
 made_in VARCHAR(45) NOT NULL,
 price INT NOT NULL,
 company VARCHAR(40) NOT NULL,
 expiration_date DATE NOT NULL,
 type FRUIT NOT NULL
);

-- 

CREATE TABLE films (
 id INT NOT NULL UNIQUE,
 title VARCHAR(50) NOT NULL UNIQUE,
 genre VARCHAR(20) NOT NULL CHECK( character_length(genre) < 2),
 duration real,
 author VARCHAR(30) NOT NULL,
 rate real check(rate > 1.0 and 10.0 > rate),
 country VARCHAR(50) NOT NULL
);


-- 1.4
CREATE TABLE Employees (
    employee_id VARCHAR(15) NOT NULL UNIQUE,
    irth_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    job_title VARCHAR(30) NOT NULL,
    hire_date VARCHAR(25) NOT NULL,
    alary VARCHAR(9) NOT NULL
);

-- 
CREATE TABLE Books (
 book_id VARCHAR(30) NOT NULL PRIMARY KEY,
 title VARCHAR(50) NOT NULL,
 author VARCHAR(40) NOT NULL,
 publication_year DATE NOT NULL,
 genre VARCHAR(20) NOT NULL CHECK( character_length(genre) < 4),
 isbn BIGINT NOT NULL
);
-- 
CREATE TABLE Customers (
 customer_id VARCHAR(30) NOT NULL PRIMARY KEY,
 firth_name VARCHAR(20) NOT NULL,
 last_name VARCHAR(20) NOT NULL,
 email VARCHAR(60),
 phone_number BIGINT NOT NULL,
 address VARCHAR(50)
);