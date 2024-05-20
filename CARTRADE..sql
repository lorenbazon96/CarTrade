CREATE DATABASE CarTrade;
USE CarTrade;

CREATE TABLE Car (
    id INT PRIMARY KEY AUTO_INCREMENT,
    brand VARCHAR(100),
    model VARCHAR(100),
    year INT,
    price FLOAT
);

CREATE TABLE FuelRecord (
    id INT PRIMARY KEY AUTO_INCREMENT,
    car_id INT,
    fuel_quantity FLOAT,
    fuel_type VARCHAR(50),
    price_per_unit FLOAT,
    total_cost FLOAT,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (car_id) REFERENCES Car(id)
);

CREATE TABLE MaintenanceRecord (
    id INT PRIMARY KEY AUTO_INCREMENT,
    car_id INT,
    maintenance_type VARCHAR(100),
    description TEXT,
    cost FLOAT,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (car_id) REFERENCES Car(id)
);
