#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound


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

    # Access Database and print
    try:
        state = session.query(State.id, State.name).filter(State.id == 1).one()
        print(state)
    except MultipleResultsFound:
        pass
    except Exception:
        print("Nothing")
    # Close Session
    session.close()
