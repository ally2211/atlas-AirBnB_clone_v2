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
        cities = relationship("City", backref="state")
    else:
        name = ""
        _cities = []

    @property
    def cities(self):
        """Returns the list of City objects from storage linked to the current State."""
        if models.storage_t != "db":
            # Assuming there's a global storage object where all cities are stored
            # and each city object has a 'state_id' attribute to link it to its state.
            return [city for city in models.storage.all('City').values() if city.state_id == self.id]
        else:
            # When using db storage, the _cities relationship provides the city objects
            return self._cities
        