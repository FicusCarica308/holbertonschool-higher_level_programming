#!/usr/bin/python3
"""
Descr:
> Takes 3 arguments: mysql username, mysql password and database name
> import State and Base from model_state
> connects to a MySQL server running on localhost at port 3306
> output fist state in states by states.id without calling .all()

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
    result = session.query(State).order_by(State.id).first()
    # ^^^^^^querys all object entrys in DB
    if (result is not None):
        print("{}: {}".format(result.id, result.name))
    else:
        print("Nothing")
    session.close()
