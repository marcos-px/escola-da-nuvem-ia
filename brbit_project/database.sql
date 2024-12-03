CREATE DATABASE cadastro_clientes;

USE cadastro_clientes;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255),
    cep VARCHAR(8),
    endereco TEXT
);