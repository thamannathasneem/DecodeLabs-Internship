CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER,
    city TEXT
);

INSERT INTO employees VALUES
(1, 'Ayesha', 'Developer', 50000, 'Hyderabad'),
(2, 'Rahul', 'Designer', 40000, 'Delhi'),
(3, 'Sneha', 'Developer', 60000, 'Mumbai'),
(4, 'Arjun', 'Marketing', 45000, 'Chennai'),
(5, 'Zara', 'Developer', 70000, 'Hyderabad'),
(6, 'Kiran', 'Marketing', 48000, 'Delhi');

SELECT * FROM employees;

SELECT * FROM employees
WHERE department = 'Developer';

SELECT * FROM employees
WHERE salary > 50000;

SELECT * FROM employees
ORDER BY salary DESC;

SELECT * FROM employees
ORDER BY salary ASC;

SELECT department, COUNT(*) AS total_employees
FROM employees
GROUP BY department;

SELECT COUNT(*) AS total_employees
FROM employees;

SELECT SUM(salary) AS total_salary
FROM employees;

SELECT AVG(salary) AS average_salary
FROM employees;

SELECT city, AVG(salary) AS average_salary
FROM employees
GROUP BY city;

SELECT city, AVG(salary) AS average_salary
FROM employees
WHERE salary > 45000
GROUP BY city
ORDER BY average_salary DESC;

SELECT * FROM employees
WHERE city = 'Delhi';

SELECT * FROM employees
WHERE city LIKE 'H%';

SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department;

SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department;