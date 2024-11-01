#!/usr/bin/python3
"""Script to list all City objects from the database along with their State.

Connects to a MySQL database, retrieves all City objects and their associated
State names, and prints them in a specific format.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":

    """Connect to the database"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).join(State)
    for city, state in query.all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.commit()

    session.close()
