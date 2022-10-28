import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    favoritePlanet = Column(String(50), ForeignKey("favPlanet.name"))
    child = relationship("favPlanet")
    favoriteCharacter = Column(String(50), ForeignKey("favChar.name"))
    child = relationship("favChar")

    def serialize(self):
        return {
            "id" : self.id,
            "username" : self.username,
            "email" : self.email
        }

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    url = Column(String(150), nullable=True)
    diameter = Column(String(15), nullable=False)
    population = Column(String(18), nullable=False)
    children = relationship("Favorite")

    def serialize(self):
        return{
            "id" : id.self,
            "name" : name.self,
            "url" : url.self,
            "diameter" : diameter.self,
            "population" : population.self
        }

class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    url = Column(String(150), nullable=True)
    birth_year = Column(String(15), nullable=False)
    homeworld = Column(String(18), nullable=False)
    children = relationship("favChar")

    def serialize(self):
        return{
            "id" : id.self,
            "name" : name.self,
            "url" : url.self,
            "birth_year" : birth_year.self,
            "homeworld" : homeworld.self
        }

class FavoritePlanet(Base):
    __tablename__ = 'favPlanet'

    id = Column(Integer, primary_key=True)
    parentId = Column(Integer, ForeignKey("planet.id"))
    name = Column(String(50), ForeignKey("planet.name"))

    def serialize(self):
        return {
            "id" : id.self,
            "name" : name.self
        }

class FavoriteCharacter(Base):
    __tablename__ = 'favChar'

    id = Column(Integer, primary_key=True)
    parentId = Column(Integer, ForeignKey("character.id"))
    name = Column(String(50), ForeignKey("character.name"))

    def serialize(self):
        return {
            "id" : id.self,
            "name" : name.self
        }

#class Address(Base):
   # __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    #id = Column(Integer, primary_key=True)
    #street_name = Column(String(250))
    #street_number = Column(String(250))
    #post_code = Column(String(250), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    #def to_dict(self):
    #    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')