#!/usr/bin/python3
'''
Module defines a City class
'''

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    '''
    City model definition
    '''
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)

    def __init__(self, name):
        '''
        Initialize new Class object
        '''
        self.name = name
