#!/usr/bin/python3
"""
Description:
    In the module we are creating a SQLALchemy class called
Citys that inherits from Base which is imported from model_state.py
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Summary:
    links to the MySQL table cities
    class attribute id column - auto-gen, not Null, primary
    class attribute name column - not Null
    class attribute state_id column - not Null, ForeignKey linked to states.id
    Args:
        Base: Base AKA declarative_base imported from model_state
    """
    __tablename__ = "cities"
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer,
                      ForeignKey('states.id'), nullable=False)
