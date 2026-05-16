#!/usr/bin/python3
"""
Lists all State objects containing 'a' from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create the engine to connect to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class and instantiate it
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects containing the letter 'a' and order by states.id
    states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()

    # Display results in the required format
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
