-- Cript that creates a database called hbtn_0d_usa and a table called states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa.states (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256));
