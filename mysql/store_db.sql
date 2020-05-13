CREATE DATABASE IF NOT EXISTS store_db;
USE store_db;

CREATE TABLE IF NOT EXISTS zips(
	zip VARCHAR(6) NOT NULL,
    z_city VARCHAR(35) NOT NULL,
    z_state VARCHAR(35) NOT NULL,
    PRIMARY KEY (zip)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS clients(
	id_client INT NOT NULL AUTO_INCREMENT,
    c_fname VARCHAR(35) NOT NULL,
	c_sname1 VARCHAR(35) NOT NULL,
    c_sname2 VARCHAR(35),
    c_street VARCHAR(35) NOT NULL,
    c_noext VARCHAR(7) NOT NULL,
    c_noint VARCHAR(7),
    c_col VARCHAR(50),
    c_zip VARCHAR(6),
    c_email VARCHAR(20),
    c_phone VARCHAR(13),
    PRIMARY KEY (id_client),
    CONSTRAINT fkzip_clients FOREIGN KEY(c_zip) 
    REFERENCES zips(zip) 
    ON DELETE SET NULL
    ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS products(
    id_product INT NOT NULL AUTO_INCREMENT,
    p_name VARCHAR(35) NOT NULL,
    p_brand VARCHAR(35) NOT NULL,
    p_descrip VARCHAR(250),
    p_price FLOAT NOT NULL,
    PRIMARY KEY(id_product)
)ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS orders(
	id_order INT NOT NULL AUTO_INCREMENT,
    id_client INT,
	o_status ENUM ('PROSESSING','ACEPTD','SENT','RECEIVED') NOT NULL,
    o_date DATE NOT NULL, 
    o_total FLOAT NOT NULL,
	PRIMARY KEY(id_order),
    CONSTRAINT fkclient_orders
    FOREIGN KEY (id_client)
    REFERENCES clients(id_client)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS order_details(
	id_order INT NOT NULL,
    id_product INT NOT NULL,
    od_amount INT NOT NULL,
    od_total DATE NOT NULL,
    PRIMARY KEY(id_order, id_product),
    CONSTRAINT fkorder_ods
    FOREIGN KEY (id_order)
    REFERENCES orders(id_order)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fkproduct_ods
    FOREIGN KEY (id_product)
    REFERENCES products(id_product)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=INNODB;

