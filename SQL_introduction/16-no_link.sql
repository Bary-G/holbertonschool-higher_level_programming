-- second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND TRIM(name) != ''
ORDER BY score DESC;