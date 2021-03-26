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
./4-cities_by_state.py (user)(password)(database name)
"""
import sys
import MySQLdb


if __name__ == "__main__":
    city_data = MySQLdb.connect(host="localhost",
                                port=3306,
                                user=sys.argv[1],
                                passwd=sys.argv[2],
                                db=sys.argv[3])
    city_cur = city_data.cursor()
    city_cur.execute("SELECT cities.id, cities.name, states.name\
                     FROM states RIGHT JOIN cities ON\
                     states.id=cities.state_id ORDER BY cities.id ASC")
    rows = city_cur.fetchall()
    for row in rows:
        print(row)
    city_cur.close()
    city_data.close()
