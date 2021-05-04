#!/usr/bin/python3
"""
Descr:
> Takes 3 arguments: mysql username, mysql password and database name
> import State and Base from model_state
> connects to a MySQL server running on localhost at port 3306
> finds all state objects in given database that contain the letter 'a'
and deletes them from the table
"""
from sys import argv as av
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


if __name__ == "__main__":
    # ====Engine creation====
    engine_args = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(av[1],
                                                                   av[2],
                                                                   av[3])
    states_engine = create_engine(engine_args)
    # ====session creation====
    session_obj = sessionmaker(states_engine)
    session = session_obj()
    # ====session query (locates objects with states.name that have 'a')====
    results = session.query(State).filter(State.name.like("%a%")).\
        order_by(State.id).all()
    # ====deletion from results====
    for result in results:
        session.delete(result)
    # ====commit and close====
    session.commit()
    session.close()
