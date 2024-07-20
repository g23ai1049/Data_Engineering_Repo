-- 1. Using Partitioning:
SELECT company, COUNT(*) AS job_count
FROM linkedin_transformed_data
WHERE job_type = 'Onsite' AND search_country = 'United States'
GROUP BY company
ORDER BY job_count DESC;

-- 2. Limit Data Scanned
SELECT job_title, COUNT(*) AS count
FROM linkedin_transformed_data
WHERE search_country = 'United States' AND job_type = 'Remote'
GROUP BY job_title
ORDER BY count DESC;

-- 3. Use Projection:
SELECT job_title, company
FROM linkedin_transformed_data
WHERE job_type = 'Onsite' AND search_country = 'United States';
