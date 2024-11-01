#!/usr/bin/python3
"""Script to retrieve and display the first
state from a MySQL database using SQLAlchemy.

This script connects to a MySQL database, retrieves the first state, and
prints its id and name. If no states are found, it prints "Nothing".
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

    first_instance = session.query(State).order_by(State.id).first()
    if first_instance:
        print("{}: {}".format(first_instance.id, first_instance.name))
    else:
        print("Nothing")

    session.close()
