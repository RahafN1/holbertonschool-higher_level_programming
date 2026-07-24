#!/usr/bin/python3
"""Script that creates the State California with the City San Francisco."""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_ca = State(name="California")
    session.add(state_ca)

    city_sf = City(name="San Francisco")
    state_ca.cities.append(city_sf)

    session.add(state_ca)
    session.commit()

    session.close()
