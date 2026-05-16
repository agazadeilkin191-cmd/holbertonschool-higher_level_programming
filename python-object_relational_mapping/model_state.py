#!/usr/bin/python3
"""
This module defines a State class and an instance Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class links to the MySQL table states.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
