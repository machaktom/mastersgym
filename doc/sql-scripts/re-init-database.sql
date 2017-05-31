DROP DATABASE IF EXISTS mgbudget;
DROP USER IF EXISTS mgadmin;

CREATE USER mgadmin WITH PASSWORD 'foo123';
CREATE DATABASE mgbudget;
GRANT ALL PRIVILEGES ON DATABASE mgbudget TO mgadmin;
