-- task 9 lists all ciries in the database
SELECT cities.id, cities.name, states.name FROM cities JOIN states ORDER BY cities.id ASC;
