#!/usr/bin/python3
"""
Descr:
> Takes 3 arguments: mysql username, mysql password and database name
> import State and Base from model_state
> connects to a MySQL server running on localhost at port 3306
> lists all City objects contained in the database
    hbtn_0e_101_usa using only the relation ship
    between State and City
> how it works: When the results of the query are passed
    there is a second list indexed list within the first
    that can be iterated through
"""
from sys import argv as av
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


if __name__ == "__main__":
    # ====engine connection/assignment=====
    engine_args = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(av[1],
                                                                   av[2],
                                                                   av[3])
    states_engine = create_engine(engine_args)
    Base.metadata.create_all(states_engine)
    # ====Session Stuff====
    session_obj = sessionmaker(states_engine)
    session = session_obj()
    # ====Collecting all States====
    result = session.query(State).all()
    cool = result[0].cities[0]
    # ==== Prints out in given format using relationship ====
    for state in result:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
    # ==== close ====
    session.close()
