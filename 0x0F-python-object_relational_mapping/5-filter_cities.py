#!/usr/bin/python3
"""
Description:
Here we have a program that opens a MySQL database from arguments
passed on exectution. Host name and port number are static
to local host system.
===================================================================
MySQL Execution:
Will print results from query in ascending order by id of city
entrys. Uses JOIN on state and citie.state id's
===================================================================
USAGE:
./5-filter_cities.py (user)(password)(database name)(state name)
SAFE FUNCTION !!!!!
"""
import sys
import MySQLdb


if __name__ == "__main__":
    no_output = 0  # used to flag if output is found or not 0 if no 1 if yes
    city_data = MySQLdb.connect(host="localhost",
                                port=3306,
                                user=sys.argv[1],
                                passwd=sys.argv[2],
                                db=sys.argv[3])
    city_cur = city_data.cursor()
    city_cur.execute("SELECT cities.name\
                     FROM states RIGHT JOIN cities ON\
                     states.id=cities.state_id WHERE states.name=%s\
                     ORDER BY cities.id ASC", (sys.argv[4],))
    rows = city_cur.fetchall()
    for row in rows:
        print(row[0], end="")
        if row != rows[-1]:
            print(", ", end="")
        else:
            no_output = 1  # signals that output has been found
            print()
    if (no_output == 0):  # prints if no output is found
        print()
    city_cur.close()
    city_data.close()
