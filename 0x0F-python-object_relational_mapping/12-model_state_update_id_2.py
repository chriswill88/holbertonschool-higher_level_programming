#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # setting up connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]), pool_pre_ping=True)

    # Creating Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Access Metadata - issues create statements for tables
    Base.metadata.create_all(engine)

    # update state and print
    state = session.query(State).filter(State.id == 2).one()
    state.name = 'New Mexico'
    session.commit()

    # Close Session
    session.close()
