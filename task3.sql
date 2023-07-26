-- 1
SELECT COUNT(country) FROM people WHERE country LIKE '%stan';
SELECT country, count(*) FROM people GROUP BY country;

-- 2
SELECT date_of_birth, count(date_of_birth) 
FROM students 
GROUP BY date_of_birth 
HAVING count(*) > 1;

-- 3
SELECT university, count(university) 
FROM students 
GROUP BY university 
HAVING count(*) > 1;

-- 4
SELECT country, count(is_married) 
FROM people 
WHERE is_married='true' 
GROUP BY country, is_married
HAVING count(is_married) > 0;

-- 5
SELECT name, price, count(price) as price
FROM products
GROUP BY name, price
HAVING count(*) > 1;

-- 6
SELECT type, count(type) as product_type
FROM products
GROUP BY type
HAVING count(*) > 1;

-- 7
SELECT genre, count(genre) as genre_rate
FROM films
WHERE rate >= 5
GROUP by genre
HAVING count(*) > 1;

-- 8
SELECT country, rate, count(rate) as rate_count
from films
GROUP by country, rate
HAVING count(*) > 1;