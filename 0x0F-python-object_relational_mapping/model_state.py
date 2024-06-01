#!/usr/bin/python3
"""state model module"""

import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """state model"""
    __tablename__ = 'states'
    id = Column('id', Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column('name', String(128), nullable=False)
