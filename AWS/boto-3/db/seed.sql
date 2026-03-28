-- USERS
INSERT INTO users (name, email) VALUES
('Ismail Khan', 'ismail.khan@example.com'),
('Salman Shaikh', 'salman.shaikh@example.com'),
('Rahul Sharma', 'rahul.sharma@example.com'),
('Sravani Reddy', 'sravani.reddy@example.com');

-- PRODUCTS
INSERT INTO products (name, price, stock) VALUES
('Laptop', 75000, 10),
('Phone', 30000, 20),
('Headphones', 2000, 50),
('Mouse', 800, 100);

-- ORDERS
INSERT INTO orders (user_id, total_amount) VALUES
(1, 77000),
(2, 31600),
(3, 2800);

-- ORDER ITEMS
INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1, 1, 1, 75000),
(1, 3, 1, 2000),
(2, 2, 1, 30000),
(2, 4, 2, 800),
(3, 3, 1, 2000),
(3, 4, 1, 800);