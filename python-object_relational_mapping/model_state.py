#!/usr/bin/python3
"""Definition of the State class mapped to the MySQL table `states`."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Se crea una instancia de Base para definir las clases ORM
Base = declarative_base()


class State(Base):
    """State class mapped to the `states` table."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
