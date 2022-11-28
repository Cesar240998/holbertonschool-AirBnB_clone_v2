#!/usr/bin/python3
# This is the state class
import models
from models.base_model import BaseModel,Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from models import storage_t

if storage_t == "db":
    class State(BaseModel, Base):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)

        cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

else:
    class State(BaseModel):
        @property
        def cities(self):
            all_cities = models.storage.all("City")
            temp = []
            for c_id in all_cities:
                if all_cities[c_id].state_id == self.id:
                    temp.append(all_cities[c_id])

            return temp
