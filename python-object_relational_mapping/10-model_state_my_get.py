#!/usr/bin/python3

"""Script to retrieve and display the state with a specific name
from a MySQL database using SQLAlchemy.

This script connects to a MySQL database, retrieves the first state
with a name matching the argument, and prints its id. If no state
is found, it prints "Not found".
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

    instance = session.query(State).filter(State.name == sys.argv[4]).first()

    if instance is None:
        print("Not found")
    else:
        print("{}".format(instance.id))

    session.close()
