#!/usr/bin/python3
"""
Descr:
> Takes 3 arguments: mysql username, mysql password and database name
> import State and Base from model_state
> connects to a MySQL server running on localhost at port 3306
> lists all state objects in given database that contain the letter 'a'
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
    results = session.query(State).filter(State.name.like("%a%")).\
        order_by(State.id).all()
    # ^^^^^^querys all object entrys in DB and checks if they contain an 'a'
    for result in results:
        print("{}: {}".format(result.id, result.name))
    # ^^^^^^prints out each row of the result
    session.close()
