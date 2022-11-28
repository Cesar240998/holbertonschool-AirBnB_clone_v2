#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
import json
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.base_model import Base
import MySQLdb
import os
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()


class DBStorage:
    """This class manages storage of hbnb models in Database"""
    __engine = None
    __session = None
    classes = [City, State, User, Amenity, Place, Review]

    def __init__(self):
        """
            Initialize the connection with database
            ENV = test, delete all tables
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                            os.environ['HBNB_MYSQL_USER'],
                            os.environ['HBNB_MYSQL_PWD'],
                            os.environ['HBNB_MYSQL_HOST'],
                            os.environ['HBNB_MYSQL_DB']), pool_pre_ping=True)
        if "HBNB_ENV" in os.environ and os.environ["HBNB_ENV"] == "test":
            Base.metadata.drop_all(self.__engine)

    def list_to_dict(self, l):
        """
            Transform a list of objects
            into dict where
            key = class_name.id_object
            value = the object himself
        """
        d = {}
        for obj in l:
            key = obj.__class__.__name__ + '.' + obj.id
            d[key] = obj
        return d

    def all(self, cls=None):
        """
            Select Table or All table
            and all objects in dict
        """
        d = {}
        if cls is None:
            tmp_l = []
            for c in self.classes:
                for o in self.__session.query(c).all():
                    tmp_l.append(o)
            return self.list_to_dict(tmp_l)
        else:
            l = self.__session.query(cls).all()
            return self.list_to_dict(l)

    def new(self, obj):
        """
            Add new object into the database
        """
        if obj:
            self.__session.add(obj)
            # self.save()

    def save(self):
        """
            Save into database changes on the object
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            Delete the object from the database
        """
        if obj:
            self.__session.delete(obj)

    def close(self):
        """ Release any connection/transactional
            resources owned by the Session first,
            then discarding the Session itself.
        """
        self.__session.close()

    def reload(self):
        """
            Reload/create tables from class mapped
            Create a session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
