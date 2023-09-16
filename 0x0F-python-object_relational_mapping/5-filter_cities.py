#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON \
                 cities.state_id = states.id WHERE states.name LIKE %s \
                 ORDER BY cities.id", (name,))
    cities = cur.fetchall()

    for city in cities:
        if city[1] == name:
        print(", ".join(city))

    cur.close()
    db.close()
