USE sub5gd_db;

SELECT first_name, last_name, dept_name 
FROM employees 
JOIN departments ON employees.dept_id = departments.dept_id;
