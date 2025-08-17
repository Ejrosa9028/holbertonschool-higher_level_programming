-- Select the required fields: city ID, city name, and state name
SELECT cities.id, cities.name, states.name
FROM cities
    -- Perform an INNER JOIN to match cities with their corresponding states
    INNER JOIN states ON cities.state_id = states.id
    -- Sort the results by city ID in ascending order
ORDER BY cities.id ASC;