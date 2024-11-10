CREATE TABLE auth_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    rol VARCHAR(50) NOT NULL
);

DROP TABLE auth_user;

INSERT INTO api_authuser (name, password, email, username, rol) 
VALUES ('ffg', 'pbkdf2_sha256$260000$2G5uILgk2s0VJ6HFBz7UQw$XMg8ik7hC7D9vYHddVZnPDPyJ8YyZs/5UycpeJgBc4I=', 'ffg@example.com', 'FFG', 'usuario');

INSERT INTO api_authuser (password, last_login, is_superuser, username, email, is_staff, is_active, rol, name)
VALUES ('pbkdf2_sha256$260000$2G5uILgk2s0VJ6HFBz7UQw$XMg8ik7hC7D9vYHddVZnPDPyJ8YyZs/5UycpeJgBc4I=', '2024-10-29 16:11:33.496274', 0, 'ffg', 'ffg@gmail.com', 0, 1, 'user', 'Kiko');

-- Tabla projects
CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    project_responsible_id INT,
    project_client VARCHAR(255),
    project_budget DECIMAL(15, 2)
);

-- Tabla companies
CREATE TABLE companies (
    company_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    company_address VARCHAR(255),
    company_reference VARCHAR(255)
);

-- Tabla clients
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    client_name VARCHAR(255) NOT NULL,
    client_reference VARCHAR(255)
);

-- Tabla responsibles
CREATE TABLE responsibles (
    responsible_id INT AUTO_INCREMENT PRIMARY KEY,
    responsibleuser_id INT,
    responsible_name VARCHAR(255),
    responsible_username VARCHAR(255) 	
);

-- Tabla offers
CREATE TABLE offers (
    offer_id INT AUTO_INCREMENT PRIMARY KEY,
    offer_title VARCHAR(255) NOT NULL,
    offer_reference VARCHAR(255),
    offer_amount DECIMAL(15, 2),
    offer_responsible_id INT,
    offer_project_id INT,
    offer_client_id INT,
    offer_client_company VARCHAR(255),

    FOREIGN KEY (offer_project_id) REFERENCES projects(project_id),
    FOREIGN KEY (offer_client_id) REFERENCES clients(client_id)
);

ALTER TABLE offers
ADD CONSTRAINT fk_offer_responsible
FOREIGN KEY (offer_responsible_id) REFERENCES responsibles(responsible_id);

-- Agregar clave foránea de responsible_offer_id en responsibles para referenciar a offers
ALTER TABLE responsibles
ADD COLUMN responsible_offer_id INT,
ADD CONSTRAINT fk_responsible_offer
FOREIGN KEY (responsible_offer_id) REFERENCES offers(offer_id);

-- 1. Desactivar temporalmente la verificación de claves foráneas
SET FOREIGN_KEY_CHECKS = 0;

-- 2. Borrar tablas en orden inverso para evitar errores por dependencias
DROP TABLE IF EXISTS responsibles;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS offers;
DROP TABLE IF EXISTS projects;

-- 3. Volver a activar la verificación de claves foráneas
SET FOREIGN_KEY_CHECKS = 1;
