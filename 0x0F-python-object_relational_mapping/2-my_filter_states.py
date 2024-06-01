#!/usr/bin/python3
"""Filter states by user input"""
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
    cur.execute(
            "SELECT * FROM states WHERE REGEXP_LIKE(name, '{}', 'c')\
                    ORDER BY id ASC".format(arg))
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
