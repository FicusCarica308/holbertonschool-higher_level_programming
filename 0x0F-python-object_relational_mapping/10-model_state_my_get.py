#!/usr/bin/python3
"""
Descr:
> Takes 3 arguments: mysql username, mysql password and database name, state
> import State and Base from model_state
> connects to a MySQL server running on localhost at port 3306
> lists a single state object that matches the given state name
> order by ascending by state.id

Comments:
the ^^^ just means the line of code above the comment is what it
is refereing too (needed to please pep8)
"""
from sys import argv as av
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


if __name__ == "__main__":
    engine_args = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(av[1],
                                                                   av[2],
                                                                   av[3])
    states_engine = create_engine(engine_args)
    # ^^^^^creates an enginer using above args
    session_obj = sessionmaker(states_engine)
    # ^^^^^binds database(engine) to session maker
    session = session_obj()
    # ^^^^^^sets up new query session from session maker
    result = session.query(State).filter_by(name=av[4]).first()
    # ^^^^^^query for the state that is given
    if (result is not None):
        print(result.id)  # prints the id of the found state
    else:
        print("Not found")  # if state is not found
    session.close()
