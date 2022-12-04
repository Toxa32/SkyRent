"""This unit contains an Offer model to work with offers table"""
from setup.db.base_model import Base
from setup.db import db
# --------------------------------------------------------------------------


class Offer(Base):
    """The Offer class is a model to work with offers table"""
    __tablename__ = 'offers'

    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    picture_url = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    features_on = db.Column(db.PickleType, nullable=False)
    features_off = db.Column(db.PickleType, nullable=False)
    host_name = db.Column(db.String, nullable=False)
    host_phone = db.Column(db.String, nullable=False)
    host_location = db.Column(db.String, nullable=False)
