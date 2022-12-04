"""This file contains schemas to serialize SQLAlchemy models"""
from flask_restx import fields
from flask_restx.fields import String
from setup.api import api

# -----------------------------------------------------------------------


offer_schema = api.model('offer', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, example='Spacy apartments'),
    'description': fields.String(required=True, example='The building is '
                                                        'shaped like an L'),
    'picture_url': fields.String(required=True, example='https://pic.jpg'),
    'price': fields.Integer(required=True, example=300),
    'country': fields.String(required=True, example='Germany'),
    'city': fields.String(required=True, example='Berlin'),
    'features_on': fields.List(required=True, cls_or_instance=String,
                               example=['Terrace', 'Fitness']),
    'features_off': fields.List(required=True, cls_or_instance=String,
                                example=['AC', 'Netflix']),
    'host_name': fields.String(required=True, example='Brendan'),
    'host_phone': fields.String(required=True, example='367-326-6229'),
    'host_location': fields.String(required=True,
                                   example='10 Henrietta Street')
})
