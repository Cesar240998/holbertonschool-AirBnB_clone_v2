#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage
from os import getenv

if storage == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all')

else:  # File Storage
    class State(BaseModel):
        """ State class """
        name = ""

        @property
        def cities(self):
            l = []
            for k, v in storage.all(City).items():
                if v.state_id == self.id:
                    l.append(v)
            return l
