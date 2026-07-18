-- Explain about SQL upto DDL ----------------------------------------

--  SQL(Structured Query Language)
--      * DDL (Data Definition Language)
--          - defines and manages the database
--          - CREATE DATABASE, CREATE TABLE, DROP DATABASE, DROP TABLE
--          - ALTER TABLE, RENAME TABLE, TRUNCATE TABLE
--          - CREATE INDEX, DROP INDEX 
--      * DML (Data Manupulation Language)
--          - works with data inside tables
--          - INSERT INTO, UPDATE, DELETE
--      * DCL (Data Control Language)
--          - controls permissions and access
--          - GRANT, REVOKE

mysql -u root

-- Question 1 ----------------------------------------

-- Create a database named SchoolDB.
-- Use the database SchoolDB.
-- Create a table named Students with the following columns:
--      - StudentID - INT, Primary Key
--      - Name ------ VARCHAR(50)
--      - Age ------- INT
--      - Grade ----- VARCHAR(5)
-- Create a table named Teachers with the following columns:
--      - TeacherID → INT, Primary Key
--      - Name → VARCHAR(50)
--      - Subject → VARCHAR(50)

create database SchoolDB;
use SchoolDB;

create table Students (
StudentID int primary key,
Name varchar(50),
Age int,
Grade varchar(5));

create table Teachers (
TeacherID int primary key,
Name varchar(50),
Subject varchar(50));

-- Question 2 ----------------------------------------

-- Insert 5 students into the Students table
-- Insert 3 teachers into the Teachers table
-- Display all records from the Students table using SELECT *
-- Display all records from the Teachers table using SELECT *

insert into Students values
(1, 'Alice', 20, 'A'),
(2, 'Bob', 19, 'B'),
(3, 'Charlie', 21, 'A'),
(4, 'Diana', 18, 'C'),
(5, 'Ethan', 22, 'B');

insert into Teachers values
(101, 'Dr. Roy', 'Mathematics'),
(102, 'Ms. Smith', 'Biology'),
(103, 'Mr. Kumar', 'Physics');

select * from Students;
select * from Teachers;

-- Question 3 - Modifying Table Structure (DDL) ------

-- Add a new column Email to the Students table
-- Add a new column PhoneNumber to the Teachers table
-- View the table structure to check your changes
--      - (e.g., using DESCRIBE Students; in MySQL)

alter table Students add
Email varchar(50);

alter table Teachers add
PhoneNumber varchar(15);

describe Students;
describe Teachers;

-- Question 4 - eleting and Truncating (DDL) ---------

-- Remove the PhoneNumber column from the Teachers table
-- Truncate all records from the Students table but keep the table structure
-- Drop the Teachers table completely from the database

alter table Teachers drop column PhoneNumber;
truncate table Students;
drop table Teachers;