#!/usr/bin/python3
"""Lists first state from database"""

from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db = argv[3]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, db))
    session = Session(bind=engine)

    states = session.query(State).where(
            State.name.like('%a%')).order_by(State.id.asc()).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))
