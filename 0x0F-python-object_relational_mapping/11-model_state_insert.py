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

    # Add state and print
    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    # print
    try:
        state = session.query(State).filter(State.name == 'Louisiana').one()
        print("{}".format(state.id))
    except Exception:
        print("Not found")
    # Close Session
    session.close()
