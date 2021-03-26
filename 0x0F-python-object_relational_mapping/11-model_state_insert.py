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
from model_state import Base, State
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
    # ====Adding new state to table====
    new_state = State()
    new_state.id = len(session.query(State).all()) + 1
    print(new_state.id)  # prints the new states id
    new_state.name = "Louisiana"
    session.add(new_state)
    session.commit()
    session.close()
