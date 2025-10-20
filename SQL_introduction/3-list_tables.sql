-- Another yet comment
SELECT table_name
FROM information_schema.tables
WHERE table_schema = DATABASE();
