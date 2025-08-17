#!/usr/bin/python3
"""
Defines a State class and creates a SQLAlchemy Base instance.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Create the Base class
Base = declarative_base()


class State(Base):
    """
    State class that maps to the MySQL table 'states'.

    Attributes:
        id (int): Primary key, auto-incremented, unique, not null.
        name (str): State name, max 128 characters, not null.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
