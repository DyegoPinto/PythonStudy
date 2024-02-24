--create the database
CREATE DATABASE PYTHON

--Using SQL Auth
CREATE LOGIN python_login WITH PASSWORD = 'python';

--create the user from the login
Use PYTHON
CREATE USER python FOR LOGIN python_login

--To give user SELECT/UPDATE/INSERT/DELETE on all tables
EXEC sp_addrolemember 'db_datareader', 'python'
EXEC sp_addrolemember 'db_datawriter', 'python'
EXEC sp_addrolemember 'db_ddladmin'  , 'python'

select @@SERVERNAME