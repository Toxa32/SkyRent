"""This file contains CBVs to work with requests like /locations/"""
from flask_restx import Namespace, Resource
from container import offers_service
# -------------------------------------------------------------------------
location_ns = Namespace('locations')
# -------------------------------------------------------------------------


@location_ns.route('/')
class LocationsView(Resource):
    """The LocationsView is a CBV to work with routes like /locations/"""

    def get(self) -> tuple:
        """This method processes a GET requests

        :returns: a list of dictionaries containing country and city info
        """
        return offers_service.get_country_and_city(), 200
