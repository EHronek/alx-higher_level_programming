#!/usr/bin/python3
import sys
import MySQLdb
"""takes in the name of states as an argument and lists all cities of the
state"""
if __name__ == '__main__':
    db_conn = MySQLdb.connect(
        host='localhost',
	user=sys.argv[1],
	passwd=sys.argv[2],
	port=3306,
	db=sys.argv[3]
    )
    c = db_conn.cursor()
    state_name_clean = sys.argv[4].replace("'", "''")
    c.execute("""
    SELECT cities.name
    FROM cities
    JOIN states
    ON state_id=states.id
    WHERE states.name LIKE BINARY %s
    ORDER BY cities.id
    """, (state_name_clean,))
    rows = c.fetchall()

    for row in rows:
        print(row[0])
