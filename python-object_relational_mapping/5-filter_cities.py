#!/usr/bin/python3

"""Script to connect to a MySQL database and retrieve cities with their
associated states using a join operation."""

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
    state_name = sys.argv[4]
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s ORDER BY cities.id ASC", (state_name,)
    )

    results = cursor.fetchall()

    city_names = [row[0] for row in results]

    print(", ".join(city_names))

    cursor.close()
    db.close()
