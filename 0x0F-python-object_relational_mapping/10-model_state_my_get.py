#!/usr/bin/python3
"""Get a state from database with name"""

from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db = argv[3]
    arg = argv[4]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, db))
    session = Session(bind=engine)

    state = session.query(State).where(State.name.like(arg)).scalar()
    if state is not None:
        print(state.id)
    else:
        print('Not found')
