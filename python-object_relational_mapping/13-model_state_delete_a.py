#!/usr/bin/python3

"""Script to delete State objects containing the letter 'a'
from the database hbtn_0e_6_usa.

Connects to a MySQL database, finds all State objects with names
containing the letter 'a', and deletes them.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":

    """Connect to the database"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(State.name.contains('a')):
        session.delete(instance)
    session.commit()

    session.close()
