-- this script list all records of the table second_table if nae is not null
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
