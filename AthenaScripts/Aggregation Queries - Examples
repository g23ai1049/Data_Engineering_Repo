-- Example 1: Count Job Postings by Job Type

SELECT job_type, COUNT(*) AS job_count
FROM linkedin_transformed_data
GROUP BY job_type;

-- Example 2: Top Companies by Number of Job Postings

SELECT company, COUNT(*) AS job_count
FROM linkedin_transformed_data
GROUP BY company
ORDER BY job_count DESC
LIMIT 10;

