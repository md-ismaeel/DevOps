CREATE TABLE
    IF NOT EXISTS users (
        id INT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255),
        role VARCHAR(255)
    );


INSERT INTO
    users (id, name, email, password, role)
VALUES
    (1, 'John Doe', 'B2aYD@example.com', 'password123', 'superadmin'),
    (2, 'Jane Smith', 'V4L0P@example.com', 'password456', 'admin');
    (3, 'Bob Johnson', 'wWd0A@example.com', 'password789', 'user');

CREATE TABLE
    IF NOT EXISTS orders (
        id INT PRIMARY KEY,
        user_id INT,
        order_total DECIMAL(10, 2),
        FOREIGN KEY (user_id) REFERENCES users (id)
    );

INSERT INTO
    orders (id, user_id, order_total)
VALUES
    (1, 1, 100.00),
    (2, 2, 50.00);
    (3, 3, 200.00);


CREATE TABLE
    IF NOT EXISTS products (
        id INT PRIMARY KEY,
        name VARCHAR(255),
        description TEXT,
        price DECIMAL(10, 2)
    );


INSERT INTO
    products (id, name, description, price)
VALUES
    (1, 'Product A', 'Description for Product A', 10.99),
    (2, 'Product B', 'Description for Product B', 19.99),
    (3, 'Product C', 'Description for Product C', 5.99);