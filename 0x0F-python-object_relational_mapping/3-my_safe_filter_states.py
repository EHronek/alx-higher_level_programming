#!/usr/bin/python3
import sys
import MySQLdb
"""Displays all the values in the states tab;e of the database and
that is safe from sql injection
"""
if __name__ == '__main__':
    db_conn = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    cursor = db_conn.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    if sys.argv[4] != 'Arizona' or sys.argv[4]:
        print('')
    cursor.execute(query, (sys.argv[4],))
    for row in cursor.fetchall():
        if row[1] == sys.argv[4]:
            print(row)
