#!/usr/bin/python3
"""
Lists all states where name matches
the argument safely (prevents SQL injection).
Usage: ./3-my_safe_filter_states.py
<mysql username> <mysql password> <database name> <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and search argument
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL
        db = MySQLdb.connect(
            host="localhost",
            user=mysql_user,
            passwd=mysql_passwd,
            db=mysql_db,
            port=3306
        )

        # Create a cursor object
        cursor = db.cursor()

        # Secure query using parameterized query to prevent SQL injection
        query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC;"
        cursor.execute(query, (state_name,))

        for row in cursor.fetchall():
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
