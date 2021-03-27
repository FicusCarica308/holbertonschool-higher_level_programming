#!/usr/bin/python3
"""
Descr:
> Takes 3 arguments: mysql username, mysql password and database name
> import State and Base from model_state
> connects to a MySQL server running on localhost at port 3306
>  prints all City objects from the database hbtn_0e_14_usa sorted
    in ascending order by cities.id
Output:
<state name>: (<city id>) <city name>
"""
from sys import argv as av
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, join, outerjoin


if __name__ == "__main__":
    # ====Engine creation====
    engine_args = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(av[1],
                                                                   av[2],
                                                                   av[3])
    states_engine = create_engine(engine_args)
    # ====session setup====
    session_obj = sessionmaker(states_engine)
    session = session_obj()
    # ====Session Querry====
    cities = session.query(State, City).join(City).order_by(City.id).all()
    # ^joins states and cities tables together using .join() using relationship
    for state, city in cities:  # prints out objects in fromat
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
