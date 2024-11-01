#!/usr/bin/python3
"""Script to retrieve and display states containing the letter 'a'
from a MySQL database using SQLAlchemy.

This script connects to a MySQL database, retrieves all states with
names containing the letter 'a', and prints their id and name.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(State.name.contains('a')):
        print('{0}: {1}'.format(instance.id, instance.name))

    session.close()
