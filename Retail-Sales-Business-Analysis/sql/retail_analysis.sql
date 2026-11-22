-- Adapt table and column names after choosing your dataset.
SELECT COUNT(*) AS transaction_rows FROM retail_sales;

-- Example templates (uncomment and adapt):
-- SELECT product_category, SUM(sales_amount) AS revenue
-- FROM retail_sales GROUP BY product_category ORDER BY revenue DESC;
-- SELECT region, SUM(sales_amount) AS revenue
-- FROM retail_sales GROUP BY region ORDER BY revenue DESC;
