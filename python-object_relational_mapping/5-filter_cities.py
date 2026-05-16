#!/usr/bin/python3
"""
This module provides a script that takes in the name of a state
as an argument and lists all cities of that state from the database.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name LIKE BINARY %s "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(query, (sys.argv[4],))
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()
