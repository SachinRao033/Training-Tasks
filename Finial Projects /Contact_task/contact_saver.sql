Create Database contacts;
Use contacts;

Create table contact_saver (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(20) NOT NULL,
phone INT NOT NULL UNIQUE,
email VARCHAR(50) NOT NULL UNIQUE
)

SELECT * FROM contact_saver;
INSERT INTO contact_saver (name,phone,email)
VALUES("Sachu",234561223,"sachu@gmail.com");



