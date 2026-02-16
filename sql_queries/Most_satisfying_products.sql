SELECT product_name,
       category,
       AVG(rating) AS avg_rating,
       COUNT(review_id) AS total_reviews
FROM processed
GROUP BY product_name, category
ORDER BY avg_rating ASC
LIMIT 20;
