#!/usr/bin/python3
"""Get all states"""
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    conn.close()
