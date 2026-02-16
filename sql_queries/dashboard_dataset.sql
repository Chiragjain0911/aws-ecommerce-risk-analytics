CREATE TABLE dashboard_dataset AS
SELECT
    product_id,
    product_name,
    category,

    ROUND(AVG(rating), 2) AS avg_rating,
    ROUND(AVG(discount_percentage), 2) AS avg_discount,
    COUNT(review_id) AS total_reviews,

    ROUND(
        SUM(CASE WHEN rating <= 3 THEN 1 ELSE 0 END) * 1.0 
        / COUNT(review_id),
    2) AS complaint_ratio,

    CASE
        WHEN AVG(rating) <= 3.5 
             AND AVG(discount_percentage) > 40
             AND SUM(CASE WHEN rating <= 3 THEN 1 ELSE 0 END) * 1.0 / COUNT(review_id) > 0.5
        THEN 'High Risk'

        WHEN AVG(rating) <= 3.5
        THEN 'Medium Risk'

        ELSE 'Low Risk'
    END AS risk_level

FROM processed
GROUP BY product_id, product_name, category