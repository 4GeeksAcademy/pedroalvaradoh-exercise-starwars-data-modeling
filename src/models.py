import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(12), nullable=False)


class Character(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    eye_color = Column(String(20))
    birth_year = Column(Integer, nullable=False)
    


class Planet(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    population = Column(Integer)
    diameter = Column(Integer)


class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    director = Column(String)
    year_released = Column(Integer)


class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    character_id = Column(String, ForeignKey('characters.name'))
    planet_id = Column(String, ForeignKey('planets.name'))
    film_id = Column(String, ForeignKey('films.title'))

    user = relationship(User)
    character = relationship(Character)
    planet = relationship(Planet)
    film = relationship(Film)


def to_dict(self):
    return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
