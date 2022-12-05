"""This file contains CBVs to work with user's requests"""
from flask import request, jsonify
from flask_restx import Namespace, Resource
from container import offers_service
from setup.api.schemas import offer_schema
# -------------------------------------------------------------------------
real_estate_ns = Namespace('offers')
# -------------------------------------------------------------------------


@real_estate_ns.route('/')
class OffersView(Resource):
    """The OffersView is a CBV to work with routes like /offers/"""
    @real_estate_ns.marshal_with(offer_schema, as_list=True,
                                 description='OK', code=200)
    def get(self) -> tuple:
        """This method processes a GET requests

        :returns: a list of serialized data and a status code
        """
        filters = request.args

        return offers_service.get_all(**filters), 200


@real_estate_ns.route('/<int:offer_id>')
class OfferView(Resource):
    """The OfferView is a CBV to work with routes like /offers/<offer_id>"""
    @real_estate_ns.marshal_with(offer_schema, code=200, description='OK')
    def get(self, offer_id: int) -> tuple:
        """This method processes a GET requests

        :returns: a serialized model and a status code
        """

        return offers_service.get_one(offer_id), 200
