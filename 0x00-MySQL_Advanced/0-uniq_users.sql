-- Creates a table users with attributes
-- id, email, name
CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
