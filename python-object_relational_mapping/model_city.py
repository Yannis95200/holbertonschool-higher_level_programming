#!/usr/bin/python3
"""Module defining the City class for SQLAlchemy ORM.

This class represents the 'cities' table in the database,
with columns id, name, and state_id.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()

class City(Base):
    """Class representing a city linked to a state in the database."""

    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
