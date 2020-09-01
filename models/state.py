#!/usr/bin/python3
""" State Module for HBNB project """

import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import (Column, String, Integer)
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class
    returns the list of City instances with state_id equals to the
    current State.id"""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """This function: getter attribute cities that returns the list of
            City instances with state_id equals to the current State.id => It
            will be the FileStorage relationship between State and"""
            all_cities = models.storage.all(City)
            result = [city for city in all_cities.values() if city.state_id == self.id]
            return result
