"""This unit contains a Base model to inherit"""
from sqlalchemy import Column

from setup.db import db
# ------------------------------------------------------------------------


class Base(db.Model):
    """The Base class is a model helping creates another models"""
    __abstract__ = True

    id = Column(db.Integer, primary_key=True, autoincrement=True)
