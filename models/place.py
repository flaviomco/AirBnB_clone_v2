#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review",
                               cascade="all, delete",
                               backref="place")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """getter for reviews"""
            reviews_list = models.storage.all(Review)
            new_list = []
            for key, value in reviews_list.items():
                if value.amenity_id == self.id:
                    new_list.append(value)
            return new_list

        @property
        def amenities(self):
            """getter for amenities"""
            amenity_list = models.storage.all(Amenity)
            new_list = []
            for key, value in amenity_list.items():
                if value.place_id == self.id:
                    new_list.append(value)
            return new_list

        @amenities.setter
        def amenities(self, value):
            """setter for amenities"""
            if type(value) is Amenity:
                self.amenity_ids.append(value.id)
