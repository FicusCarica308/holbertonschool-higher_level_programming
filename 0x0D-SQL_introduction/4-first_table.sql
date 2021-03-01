-- creates a new table in the current database (signified by -p option)
-- cat 3-list_tables.sql | mysql -hlocalhost -uroot -p [DATABASE-NAME]
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
