#!/usr/bin/python3
import sys
import MySQLdb
"""Displays all the values in the states tab;e of the database and
that is safe from sql injection
"""
if __name__ == '__main__':
    user, password, database, state = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=user, passwd=password, db=database)
    db = db.cursor()
    db.execute("""SELECT * FROM states WHERE name=%s ORDER BY id""", (state,))
    r = db.fetchall()
    for i in r:
        print(i)
