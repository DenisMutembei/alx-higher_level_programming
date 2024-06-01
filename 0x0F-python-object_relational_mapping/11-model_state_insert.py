#!/usr/bin/python3
"""Add a new state to database"""

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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)  # doesn't get an id until it has been committed
