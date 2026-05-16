#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
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

    # Query the first State object ordered by states.id
    state = session.query(State).order_by(State.id).first()

    # Display the result or Nothing if the table is empty
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
