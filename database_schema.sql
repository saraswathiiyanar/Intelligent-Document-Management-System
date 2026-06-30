CREATE DATABASE idms;

USE idms;

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(255),
    role VARCHAR(20)
);

CREATE TABLE folders (
    folder_id INT PRIMARY KEY AUTO_INCREMENT,
    folder_name VARCHAR(100),
    created_date DATE,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE documents (
    document_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(150),
    category VARCHAR(100),
    file_type VARCHAR(20),
    upload_date DATE,
    status VARCHAR(30),
    folder_id INT,
    user_id INT,
    FOREIGN KEY (folder_id) REFERENCES folders(folder_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE document_versions (
    version_id INT PRIMARY KEY AUTO_INCREMENT,
    version_no VARCHAR(20),
    modified_date DATE,
    document_id INT,
    FOREIGN KEY (document_id) REFERENCES documents(document_id)
);