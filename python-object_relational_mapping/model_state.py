#!/usr/bin/python3
"""Module for defining the State class using SQLAlchemy.

This class represents a 'states' table in the database,
with the columns id and name.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class representing a State in the database."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
