#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db_conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM `states`")
    rows = cursor.fetchall()
    for row in rows:
       print(row)
    cursor.close()
    db_conn.close()
