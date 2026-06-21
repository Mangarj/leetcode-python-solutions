# Write your MySQL query statement below
SELECT s.student_id , s.student_name , s1.subject_name , 
      COUNT(e.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects s1
LEFT JOIN Examinations e
ON s.student_id = e.student_id AND s1.subject_name = e.subject_name
GROUP BY s.student_id,s.student_name,s1.subject_name
ORDER BY s.student_id, s1.subject_name;