#!/usr/bin/python3
"""
script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
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
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id \
                 ASC".format(name))
    states = cur.fetchall()

    for state in states:
        if state[1] == name:
            print(state)

    cur.close()
    db.close()
