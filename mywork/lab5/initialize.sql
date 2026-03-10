USE sub5gd_db;

DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(50)
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    hire_date DATETIME,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

INSERT INTO departments (dept_id, dept_name, location) VALUES
(1, 'Engineering', 'Building A'),
(2, 'Data Science', 'Building B'),
(3, 'Marketing', 'Building C'),
(4, 'HR', 'Building A'),
(5, 'Finance', 'Building B'),
(6, 'Operations', 'Building C'),
(7, 'Sales', 'Building A'),
(8, 'IT Support', 'Building B'),
(9, 'Legal', 'Building C'),
(10, 'Research', 'Building A');

INSERT INTO employees (emp_id, first_name, last_name, hire_date, dept_id) VALUES
(101, 'Ada', 'Lovelace', '2023-01-15 09:00:00', 1),
(102, 'Grace', 'Hopper', '2023-02-20 09:30:00', 2),
(103, 'Katherine', 'Johnson', '2023-03-10 10:00:00', 2),
(104, 'Margaret', 'Hamilton', '2023-04-05 08:45:00', 1),
(105, 'Alan', 'Turing', '2023-05-12 11:15:00', 10),
(106, 'John', 'Von Neumann', '2023-06-18 13:00:00', 5),
(107, 'Claude', 'Shannon', '2023-07-22 14:30:00', 8),
(108, 'Hedy', 'Lamarr', '2023-08-30 09:00:00', 10),
(109, 'Annie', 'Easley', '2023-09-14 10:45:00', 2),
(110, 'Dorothy', 'Vaughan', '2023-10-01 08:30:00', 8);