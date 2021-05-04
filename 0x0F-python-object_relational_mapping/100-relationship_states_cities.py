#!/usr/bin/python3
"""
Descr:
> Takes 3 arguments: mysql username, mysql password and database name
> import State and Base from model_state
> connects to a MySQL server running on localhost at port 3306
> will add a new state to the states table and prints the new id
Comments:
the ^^^ just means the line of code above the comment is what it
is refereing too (needed to please pep8)
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
    # ====Adding new state====
    new_id = len(session.query(State).all()) + 1
    new_state = State()
    new_state.id = new_id
    new_state.name = "California"
    session.add(new_state)
    # ====Adding new City====
    new_city = City()
    new_city.name = "San Francisco"
    new_city.state_id = new_id
    session.add(new_city)
    # ==== commit and close ====
    session.commit()
    session.close()
