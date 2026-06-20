# Write your MySQL query statement below
SELECT name ,bonus
FROM Employee left JOIN Bonus
ON Employee.empId=Bonus.empId
WHERE bonus IS NULL or bonus< 1000 ;