CREATE DATABASE sa_tienda;


CREATE TABLE product (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  image VARCHAR(255) NOT NULL,
  brand VARCHAR(255) NOT NULL,
  price DECIMAL NOT NULL,
  category VARCHAR(255) NOT NULL,
  count_in_stock INTEGER DEFAULT 0,
  description TEXT NOT NULL,
  rating INTEGER DEFAULT 0,
  num_reviews INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE "user" (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  is_admin BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);



CREATE TABLE shipping (
  id SERIAL PRIMARY KEY,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(255) NOT NULL,
  postal_code VARCHAR(255) NOT NULL,
  country VARCHAR(255) NOT NULL
);

CREATE TABLE payment (
  id SERIAL PRIMARY KEY,
  payment_method VARCHAR(255) NOT NULL
);

CREATE TABLE order_item (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  qty INTEGER NOT NULL,
  image VARCHAR(255) NOT NULL,
  price DECIMAL NOT NULL,
  product_id INTEGER REFERENCES product(id) NOT NULL
);

CREATE TABLE "order" (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES "user"(id) NOT NULL,
  items_price DECIMAL,
  tax_price DECIMAL,
  shipping_price DECIMAL,
  total_price DECIMAL,
  is_paid BOOLEAN DEFAULT FALSE,
  paid_at TIMESTAMP,
  is_delivered BOOLEAN DEFAULT FALSE,
  delivered_at TIMESTAMP,
  shipping_id INTEGER REFERENCES shipping(id),
  payment_id INTEGER REFERENCES payment(id),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE review (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  rating INTEGER DEFAULT 0,
  comment TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);


INSERT INTO product (name, image, brand, price, category, count_in_stock, description, rating, num_reviews)
VALUES
('Product 1', 'image1.jpg', 'Brand A', 9.99, 'Category 1', 10, 'Description 1', 4, 8),
('Product 2', 'image2.jpg', 'Brand B', 19.99, 'Category 2', 5, 'Description 2', 3, 2),
('Product 3', 'image3.jpg', 'Brand C', 14.99, 'Category 1', 2, 'Description 3', 5, 12),
('Product 4', 'image4.jpg', 'Brand A', 29.99, 'Category 3', 8, 'Description 4', 2, 1),
('Product 5', 'image5.jpg', 'Brand B', 39.99, 'Category 2', 0, 'Description 5', 5, 15);

INSERT INTO "user" (name, email, password, is_admin)
VALUES
('John Doe', 'john@example.com', 'password123', FALSE),
('Jane Smith', 'jane@example.com', 'securepass', TRUE),
('Alice Johnson', 'alice@example.com', 'mypassword', FALSE),
('Bob Brown', 'bob@example.com', 'pass123', FALSE),
('Eve Davis', 'eve@example.com', 'letmein', FALSE);

INSERT INTO shipping (address, city, postal_code, country)
VALUES
('123 Main St', 'City A', '12345', 'Country X'),
('456 Elm St', 'City B', '54321', 'Country Y'),
('789 Oak St', 'City C', '67890', 'Country Z'),
('321 Pine St', 'City D', '09876', 'Country X'),
('654 Cedar St', 'City E', '56789', 'Country Y');

INSERT INTO payment (payment_method)
VALUES
('Credit Card'),
('PayPal'),
('Bank Transfer'),
('Cash on Delivery'),
('Cryptocurrency');

INSERT INTO order_item (name, qty, image, price, product_id)
VALUES
('Product 1', 2, 'image1.jpg', 9.99, 1),
('Product 2', 1, 'image2.jpg', 19.99, 2),
('Product 3', 3, 'image3.jpg', 14.99, 3),
('Product 4', 1, 'image4.jpg', 29.99, 4),
('Product 5', 2, 'image5.jpg', 39.99, 5);

INSERT INTO "order" (user_id, items_price, tax_price, shipping_price, total_price, is_paid, paid_at, is_delivered, delivered_at, shipping_id, payment_id)
VALUES
(1, 59.95, 4.50, 10.00, 74.45, TRUE, '2023-06-15 10:30:00', TRUE, '2023-06-17 14:20:00', 1, 1),
(2, 19.99, 1.50, 5.00, 26.49, TRUE, '2023-06-16 12:45:00', FALSE, NULL, 2, 3),
(3, 44.97, 3.37, 7.50, 55.84, FALSE, NULL, FALSE, NULL, 3, 4),
(4, 29.99, 2.25, 5.00, 37.24, TRUE, '2023-06-17 08:10:00', FALSE, NULL, 2, 2),
(5, 79.98, 6.00, 12.50, 98.48, TRUE, '2023-06-15 15:20:00', TRUE, '2023-06-18 11:05:00', 5, 1);

INSERT INTO review (name, rating, comment)
VALUES
('User A', 4, 'Great product!'),
('User B', 2, 'Not satisfied with the quality.'),
('User C', 5, 'Highly recommended.'),
('User D', 3, 'Average product.'),
('User E', 5, 'Love it! Will buy again.');
