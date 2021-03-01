-- a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
-- state_id (FOREIGN KEY), states(id)PRIMARY KEY
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
