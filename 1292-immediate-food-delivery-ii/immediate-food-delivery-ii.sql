# Write your MySQL query statement below
SELECT
    ROUND(
        100.0 * SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS immediate_percentage
FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY customer_id
               ORDER BY order_date
           ) AS rn
    FROM Delivery
) d
WHERE rn = 1;