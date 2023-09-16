#!/usr/bin/python3
"""
This script  prints the State object with the name passed
as argument from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = "Louisiana"

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name=name)
    session.add(new_state)
    state = session.query(State).filter_by(name=name).first()

    print(str(state.id))
    session.close()
