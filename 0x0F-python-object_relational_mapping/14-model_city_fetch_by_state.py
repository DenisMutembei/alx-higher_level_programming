#!/usr/bin/python3
'''
Prints all City objects from the database hbtn_0e_14_usa
'''

from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3]))
    session = Session(bind=engine)

    result = session.query(State.name, City).join(
            State, City.state_id == State.id).order_by(City.id).all()
    for state_city in result:
        print("{}: ({}) {}".format(
            state_city[0], state_city[1].id, state_city[1].name))
