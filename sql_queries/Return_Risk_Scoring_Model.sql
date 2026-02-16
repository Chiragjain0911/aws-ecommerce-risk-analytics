SELECT product_id,
	product_name,
	category,
	COUNT(review_id) AS total_reviews,
	ROUND(AVG(rating), 2) AS avg_rating,
	ROUND(AVG(discount_percentage), 2) AS avg_discount,
	-- Complaint ratio calculation
	ROUND(
		SUM(
			CASE
				WHEN rating <= 3 THEN 1 ELSE 0
			END
		) * 1.0 / COUNT(review_id),
		2
	) AS complaint_ratio,
	-- Final Risk Classification
	CASE
		WHEN AVG(rating) <= 3.5
		AND AVG(discount_percentage) > 40
		AND SUM(
			CASE
				WHEN rating <= 3 THEN 1 ELSE 0
			END
		) * 1.0 / COUNT(review_id) > 0.5 THEN 'High Risk'
		WHEN AVG(rating) <= 3.5 THEN 'Medium Risk' ELSE 'Low Risk'
	END AS risk_level
FROM processed
GROUP BY product_id,
	product_name,
	category
ORDER BY avg_rating ASC;