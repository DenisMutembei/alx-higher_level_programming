#!/usr/bin/python3
"""Lists all cities by states"""

from sys import argv
import MySQLdb
if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=username,
                           passwd=password,
                           db=db)

    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities JOIN states \
                    ON cities.state_id = states.id \
                    ORDER BY cities.id ASC")
    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    conn.close()
