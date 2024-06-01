#!/usr/bin/python3
"""Lists all cities by state"""

from sys import argv
import MySQLdb
if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db = argv[3]
    arg = argv[4]

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=username,
                           passwd=password,
                           db=db)

    cur = conn.cursor()
    cur.execute("SELECT cities.name \
                    FROM cities JOIN states \
                    ON cities.state_id = states.id \
                    WHERE REGEXP_LIKE(states.name, '{}', 'c')\
                    ORDER BY cities.id ASC".format(
                        arg))

    cities = [city[0] for city in cur.fetchall()]

    for idx, city in enumerate(cities):
        if idx > 0:
            print(", {}".format(city), end="")
        else:
            print(city, end="")
    print()

    cur.close()
    conn.close()
