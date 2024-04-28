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
    query = 'SELECt * FROM states WHERE name = %s ORDER BY id'
    cursor.execute(query, (sys.argv[4],))
    print(cursor.fetchone())
    cursor.close()
    db_conn.close()
