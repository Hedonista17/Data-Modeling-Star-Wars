import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define Columnns for the table person
    # Notice that each Columnn is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    register_date = Column(String(150), nullable=False)
    email = Column(String(250), nullable=False , unique=True)
    

class Persona (Base):

    __tablename__ ='persona'
    id = Column(Integer, primary_key=True)
    person_name= Column(String(50), nullable=False)
    description =  Column(String(300), nullable=False)
    eye_color =Column(String(20), nullable=False)
    hair_color=Column(String(20), nullable=False)
    height= Column(Integer)

class Planeta (Base):

    __tablename__ ='planeta'
    id = Column(Integer, primary_key=True)
    planet_name= Column(String(50), nullable=False)
    description =  Column(String(300), nullable=False)
    population = Column(Integer)
    terrain = Column(String(100), nullable=False)

class Vehiculo (Base):

    __tablename__ ='vehiculo'
    id = Column(Integer, primary_key=True)
    car_name= Column(String(50), nullable=False)
    description =  Column(String(300), nullable=False)
    model = Column(String(80), nullable=False)
    film = Column(String(100), nullable=False)
    year = Column(Integer)

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define Columns for the table address.
    # Notice that each Column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer,ForeignKey('persona.id'))
    person = relationship(Persona)
    planet_id = Column(Integer,ForeignKey('planeta.id'))
    planet = relationship(Planeta)
    car_id = Column(Integer,ForeignKey('vehiculo.id'))
    car = relationship(Vehiculo)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)
    

 

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
