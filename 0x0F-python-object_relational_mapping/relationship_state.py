#!/usr/bin/python3
"""Contains the class definition of the states database"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """Database Class State"""
    __tablename__ = "states"
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
