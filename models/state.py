#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all, delete", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """getter function for cities"""
            cities_list = models.storage.all(City)
            new_list = []
            for key, value in cities_list.items():
                if value.state_id == self.id:
                    new_list.append(value)
            return new_list
