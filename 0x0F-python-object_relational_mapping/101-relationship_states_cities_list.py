#!/usr/bin/python3
"""
Descr:
> Takes 3 arguments: mysql username, mysql password and database name
> import State and Base from model_state
> connects to a MySQL server running on localhost at port 3306
> t lists all State objects, and corresponding City objects,
    contained in the database
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
    # ====Session Stuff====
    session_obj = sessionmaker(states_engine)
    session = session_obj()
    # ====Adding new state====
    results = session.query(State, City).join(City).order_by(City.id).all()
    start_name = "start"
    for state, city in results:  # prints out objects in fromat
        if (start_name != state.name):
            print("{}: {}".format(state.id, state.name))
            print("\t{}: {}".format(city.id, city.name))
            start_name = state.name
        else:
            print("\t{}: {}".format(city.id, city.name))
    # ==== close ====
    session.close()
