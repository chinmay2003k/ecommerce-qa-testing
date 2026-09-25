
-- QA Shop Database Testing Queries

-- 1. Verify product records
SELECT * FROM products;

-- 2. Verify product count
SELECT COUNT(*) AS total_products
FROM products;

-- 3. Verify product prices
SELECT name, price
FROM products;

-- 4. Find products with invalid/zero price
SELECT *
FROM products
WHERE price <= 0;

-- 5. Find duplicate product names
SELECT name, COUNT(*) AS duplicate_count
FROM products
GROUP BY name
HAVING COUNT(*) > 1;
