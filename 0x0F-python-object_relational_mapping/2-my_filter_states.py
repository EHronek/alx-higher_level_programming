#!/usr/bin/python3
"""Takes in an argument and displays all values in the states table
where name matches the argument"""
import sys
import MySQLdb

if __name__ == '__main__':
    db_conn = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='root',
        port=3306,
        db='hbtn_0e_0_usa'
    )
    cursor = db_conn.cursor()
    cursor.execute("SELECT * \
                        FROM `states` \
                        WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    for row in cursor.fetchall():
        print(row)
