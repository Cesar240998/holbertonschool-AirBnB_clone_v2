#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models import storage

#s = "HBNB_TYPE_STORAGE"
if storage == "db":
    class User(BaseModel, Base):
        """This is the class for user
        Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
        """
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")

        def __init__(self, *args, **kwargs):
            """initializes user"""
            super().__init__(*args, **kwargs)

else:
    class User(BaseModel):
        """This is the class for user
        Attributes:
        """
        email = ""
        password = ""
        first_name = ""
        last_name = ""

        def __init__(self, *args, **kwargs):
            """initializes user"""
            super().__init__(*args, **kwargs)
