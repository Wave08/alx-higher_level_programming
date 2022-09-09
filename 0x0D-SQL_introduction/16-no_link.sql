-- this script list all the records in table second_table  in hbtn_0c_0 database 
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
