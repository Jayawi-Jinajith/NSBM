mysql -u root

-- Question 1 ----------------------------------------

-- 1. Create a database named Training_Center and select it for use
-- 2. Create the following tables using suitable SQL constraints:
--      - Departments: DepartmentID (PRIMARY KEY),
--                     DepartmentName (NOT NULL and UNIQUE),
--                     Location (DEFAULT Homagama)
--      - Students: StudentID (AUTO_INCREMENT PRIMARY KEY),
--                  StudentName (NOT NULL),
--                  Email (NOT NULL and UNIQUE),
--                  Age (18-35),
--                  DepartmentID (FOREIGN KEY)
-- 3. Insert 3 department records and 5 student records
--    Display the table structures and records

create database Training_Center;
use Training_Center;

create table Departments (
DepartmentID int primary key,
DepartmentName varchar(30) unique not null,
Location varchar(50) default 'Homagama');

create table Students (
StudentID int auto_increment primary key,
StudentName varchar(30) not null,
Email varchar(30) not null unique,
Age int check(age between 18 and 35),
Department_ID int,
constraint fk_department_key foreign key (DepartmentID) references Departments(DepartmentID));

insert into Departments values 
(1,'Engineering','FOE Building'),
(2,'Computing','FOC Building'),
(3,'Business','FOB Building');

insert into Students (StudentName, Email, Age, DepartmentID) values 
('Nimal','nimal@gmil.com',18,1),
('Vinuja','vinu@gmail.com',21,3),
('Janudi','janu2026@gmail.com',22,2),
('Jane','janej@gmail.com',20,1),
('Nidul','nidul.b@gamil.com',22,2);

select * from students;
select * from Departments;

-- Question 2 ----------------------------------------

-- 1. Create Courses with
--      - CourseID (PRIMARY KEY),
--      - CourseName (NOT NULL),
--      - CourseFee (greater than 0).
-- 2. Create Enrollments with 
--      - EnrollmentID (AUTO_INCREMENT PRIMARY KEY),
--      - StudentID and CourseID (FOREIGN KEYS),
--      - EnrollmentDate (DEFAULT current date)
--    Prevent a student from enrolling in the same course twice
-- 3. Insert 3 course records and 5 enrollment records
--    Display all records

create table Courses (
CourseID varchar(5) primary key,
CourseName varchar(20) not null,
CourseFee float check(Course_Fee > 0));

create table Enrollments (
EnrollmentID int auto_increment primary key,
StudentID int,
DepartmentID int,
EnrollmentDate date default current_date,
constraint fk_student_id foreign key (StudentID) references Students(StudentID),
constraint fk_department_id foreign key (DepartmentID) references Departments(DepartmentID),
unique (StudentID, CourseID));

insert into Courses values
('C001','Software Engineering',200000),
('B001','Business Analytics',250000),
('E001','Mechanical Engineering',400000);

insert into Enrollments values
(1, 4003,1,'2025-07-01'),
(2,40002,1,default),
(3,40005,3,'2026-07-01'),
(4,40003,2,default),
(5,40001,2,'2026-04-21');

select * from Courses;
select * from Enrollments;

-- Question 3 ----------------------------------------

-- Insert a student using existing Student-ID
    insert into Students values
    (2,'Jake','jake.p@gmail.com',23,2);

-- Insert a student without Student_Name
    insert into Students (Email, Age, DepartmentID) values
    ('abc@gmail.com',21,1);

-- Insert a student with an existing Email
    insert into Students (StudentName, Email, Age, DepartmentID) values
    ('Nidul Bohara','nidul.b@gamil.com',22,2);

-- Insert a student with Age = 16
    insert into Students (StudentName, Email, Age, DepartmentID) values
    ('Nayomi','nayomi@gamil.com',16,2);

-- Insert a student using Department_ID = 99
    insert into Students (StudentName, Email, Age, DepartmentID) values
    ('Kaweesha','kwsh@gmail.com',19,99);