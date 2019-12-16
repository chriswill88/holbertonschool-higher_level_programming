#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State

"""In this Modual the table: city is being exepressed as an object"""
# Declearation base
# Base = declarative_base()


class City(Base):
    """
    class for city table
    used for creating the table itself
    """
    __tablename__ = 'cities'
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        primary_key=True,
        nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
