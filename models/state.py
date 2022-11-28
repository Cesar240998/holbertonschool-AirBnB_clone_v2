#!/usr/bin/python3
"""This is the state class"""
import models
from os import getenv
from models.base_model import BaseModel
from models.city import City, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,  Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', backref='state', cascade="all, delete")
    else:
        name = ""

    """if getenv("HBNB_TYPE_STORAGE") == "file":"""
    @property
    def cities(self):
        list_of_cities = []
        dic_cities = models.Storage.all(City)
        for city in dic_cities.items():
            if city.state_id == self.id:
                list_of_cities.append(city)
        return list_of_cities
