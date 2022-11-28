#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os
from sqlalchemy.ext.declarative import declarative_base
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",  cascade="all, delete")

    if "HBNB_TYPE_STORAGE" in os.environ \
       and os.environ['HBNB_TYPE_STORAGE'] != "db":

        @property
        def cities(self):
            """
                return the list of City objects
                from storage linked to the current State
            """
            l = []
            for k, v in models.storage.all(City).items():
                if v.state_id == self.id:
                    l.append(v)
            return l
