#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        _cities = relationship("City", backref="state")
    else:
        name = ""
        _cities = []

    @property
    def cities(self):
        """Returns list of Cities from storage linked to the current State."""
        if models.storage_t != "db":
            # from storage object where all cities are stored
            # each city object has a 'state_id' attr to link it to its state
            cities_in_state = []
            for city in models.storage.all('City').values():
                if city.state_id == self.id:
                    cities_in_state.append(city)
            return cities_in_state

        else:
            # When using db storage, the _cities rel. provides city objects
            return self._cities
