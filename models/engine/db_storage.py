#!/usr/bin/python3
"""New engine for Database"""

from sqlalchemy import create_engine, Table
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Class for db management"""
    __engine = None
    __session = None
    usr = getenv('HBNB_MYSQL_USER')
    pwd = getenv('HBNB_MYSQL_PWD')
    ht = getenv('HBNB_MYSQL_HOST')
    db = getenv('HBNB_MYSQL_DB')
    env = getenv('HBNB_ENV')

    def __init__(self):
        """constructor"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(self.usr, self.pwd, self.ht,
                                              self.db), pool_pre_ping=True)

        # Base.metadata.create_all(bind=self.__engine)

        if self.env == 'test':
            Base.metadata.delete_all(bind=self.__engine)

    def all(self, cls=None):
        """query a database session. Return a dictionary"""
        if cls is None:
            cls = "User, State, City, Amenity, Place, Review"

        obj_list = {}
        result = self.__session.query(eval(cls))

        for obj in result:
            key = obj.__class__.__name__ + '.' + obj.id
            obj_list[key] = obj
        return obj_list

    def new(self, obj):
        """add the object to database"""
        self.__session.add(obj)

    def save(self):
        """commit changes to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete given object from db"""
        if obj is not None:
            self.__session.delete(obj)
        else:
            pass

    def reload(self):
        """reload the database"""
        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Dispose the scoped session.
        First call self.__session.close() in order to release
        any connection owned by self.__session and then
        discards the session itself.
        """
        self.__session.close()
