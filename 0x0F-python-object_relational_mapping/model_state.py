#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

"""In this Modual the table: states is being exepressed as an object"""
# Declearation base
Base = declarative_base()


class State(Base):
    """
    class for states table
    used for creating the table itself
    """
    __tablename__ = 'states'
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        primary_key=True,
        nullable=False)
    name = Column(String(128), nullable=False)
