#!/usr/bin/python3
"""This is the amenity class"""
import models
from models.base_model import BaseModel,Base
from  models import storage
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

if storage == "db":
    class Amenity(BaseModel, Base):
        """
        This is the state class
        """
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)

        def __init__(self, **kwargs):
            setattr(self, "id", str(uuid4()))
            for k, v in kwargs.items():
                setattr(self, k, v)
else:
    class Amenity(BaseModel):
        """This is the class for Amenity
        Attributes:
            name: input name
        """
        name = ""
