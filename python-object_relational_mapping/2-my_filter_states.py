#!/usr/bin/python3

"""Script to connect to a MySQL database and retrieve states based on a given
name pattern from the command line arguments."""

import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY\
            '{}' ORDER BY states.id".format(sys.argv[4]))
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
