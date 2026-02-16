SELECT product_name,
       rating_count,
       COUNT(review_id) AS review_entries
FROM processed
GROUP BY product_name, rating_count
ORDER BY review_entries DESC;