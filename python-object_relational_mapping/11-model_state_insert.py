#!/usr/bin/python3

"""Script to add a new state to a MySQL database using SQLAlchemy.

This script connects to a MySQL database, adds a new state with the
name 'Louisiana', and prints the id of the new state after insertion.
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print('{}'.format(new_state.id))

    session.close()
