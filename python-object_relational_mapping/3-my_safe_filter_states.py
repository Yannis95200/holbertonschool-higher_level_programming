#!/usr/bin/python3
import MySQLdb
import sys

"""Script to connect to a MySQL database and retrieve states by exact name.
Uses command-line arguments for authentication and state name input."""

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
    )

    state_name = sys.argv[4]
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,)
    )

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
