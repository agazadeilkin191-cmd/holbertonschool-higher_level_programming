#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
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

    # Query the State object by the name passed as the 4th argument
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Display the state id or Not found if it doesn't exist
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))

    # Close the session
    session.close()
