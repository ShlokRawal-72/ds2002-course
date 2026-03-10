USE sub5gd_db;

SELECT 
    e.first_name, 
    e.last_name, 
    d.dept_name 
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE d.location = 'Building B';