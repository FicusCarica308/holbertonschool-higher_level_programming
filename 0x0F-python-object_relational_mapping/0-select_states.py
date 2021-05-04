#!/usr/bin/python3
"""
Description:
Here we have a program that opens a MySQL database from arguments
passed on exectution. Host name and port number are static
to local host system.
===================================================================
MySQL Execution:
Will print results from query in ascending order by id of state
entrys.
===================================================================
USAGE:
./0-select_states.py (user)(password)(database name)
"""
import sys
import MySQLdb


if __name__ == "__main__":
    states = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
    states_cur = states.cursor()
    states_cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = states_cur.fetchall()
    for row in rows:
        print(row)
    states_cur.close()
    states.close()
