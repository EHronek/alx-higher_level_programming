#!/usr/bin/python3
import sys
import MySQLdb
"""Displays all the values in the states tab;e of the database and
that is safe from sql injection
"""
if __name__ == '__main__':
    db_conn = MySQLdb.connect(
        host='localhost'
	user=sys.argv[1]
	passwd=sys.argv[2]
	port=3306
	db=sys.argv[3]
    )
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM states")
    for row in cursor.fetchall():
        if row[1] == sys.argv[4]
	print(row)
