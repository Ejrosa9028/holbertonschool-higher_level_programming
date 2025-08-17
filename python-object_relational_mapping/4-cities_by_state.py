#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            user=mysql_user,
            passwd=mysql_passwd,
            db=mysql_db,
            port=3306
        )

        # Create a cursor object
        cursor = db.cursor()

        # SQL query to join cities and states tables
        query = """SELECT cities.id, cities.name, states.name
                   FROM cities
                   JOIN states ON cities.state_id = states.id
                   ORDER BY cities.id ASC;"""
        cursor.execute(query)  # Execute the query

        # Fetch all results and print them
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
