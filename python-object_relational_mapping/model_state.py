#!/usr/bin/python3
"""
This module defines a State class and an instance Base = declarative_base()
This docstring ensures the module is documented properly.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table states.
    This docstring ensures the class is documented properly.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
