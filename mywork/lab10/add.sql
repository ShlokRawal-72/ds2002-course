USE sub5gd_db;

INSERT INTO departments (dept_id, dept_name, location) VALUES
(11, 'Design', 'Building C'),
(12, 'Logistics', 'Building A');

INSERT INTO employees (emp_id, first_name, last_name, hire_date, dept_id) VALUES
(111, 'Linus', 'Torvalds', '2024-01-01 09:00:00', 1),
(112, 'Tim', 'Berners-Lee', '2024-02-01 10:00:00', 11),
(113, 'Bjarne', 'Stroustrup', '2024-03-01 08:00:00', 1);
