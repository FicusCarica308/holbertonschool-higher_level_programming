#!/usr/bin/python3
"""
Descr:
> Takes 3 arguments: mysql username, mysql password and database name
> import State and Base from model_state
> connects to a MySQL server running on localhost at port 3306
> will change the states.name of any state with states.id == 2
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
    # ====loacting object with id equal to 2====
    result = session.query(State).filter_by(id=2).first()
    result.name = "New Mexico"
    # ===commiting changes and closing===
    session.commit()
    session.close()
