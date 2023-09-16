#!/usr/bin/python3
"""
This script lists all State objects from the
database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")
    session.close()
