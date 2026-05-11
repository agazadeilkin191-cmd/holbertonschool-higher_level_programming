-- lists all records of the table second_table
-- results should display the score and the name (in this order)
-- don't list rows where the name column is empty
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
