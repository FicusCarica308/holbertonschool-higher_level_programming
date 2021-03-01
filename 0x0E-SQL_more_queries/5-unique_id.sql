-- a script that creates the table unique_id on your MySQL server.
-- id has defuslt value 1 and has to be UNIQUE
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
