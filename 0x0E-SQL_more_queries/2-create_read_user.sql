-- Creates database hbtn_0d_2 and then creates user named user_0d_2
-- Gives user_0d_2 select permissions on database hbtn_0d_2 only
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
