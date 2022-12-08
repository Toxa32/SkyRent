"""This unit contains the OfferService class to work with offers table"""
from typing import List
from flask import abort
from dao.offers_dao import OfferDAO, Offer
from services.base import BaseService
from constants import METHODS
# -----------------------------------------------------------------------


class OfferService(BaseService[OfferDAO, Offer]):
    """The OfferService class provides business logic to work with user's
    requests regarding offers"""
    pass

    def get_all(self, **filters: dict) -> List[Offer]:
        """This method returns a list of all offers filtrated filters
        if ones was provided

        :param filters: a kwargs dictionary with filters to get certain offers

        :returns: a list of models
        """

        if not self._is_filters_valid(filters):
            abort(400, 'Bad Request')

        offers = self.dao.get_all(**filters)

        if not offers:
            abort(400, 'Unfortunately We have no records You are looking for')

        return offers

    @staticmethod
    def _is_filters_valid(filters: dict) -> bool:
        """This method checks if the filters are valid

        :param filters: a dictionary with filters to check

        :returns: True if the filters are valid or False otherwise
        """
        # checking provided filters and data types
        for key, value in filters.items():

            if key not in METHODS:
                return False

            if key in ('start_price', 'end_price'):

                if len(value) > 9:
                    return False

                try:
                    value = str(int(float(value)))

                except ValueError:
                    return False

            # this function used to reduce the number of validation conditions
            exec(f"""if not value.{METHODS[key]}:
                        abort(400, 'Bad Request')              
                    """)

        return True

    def get_country_and_city(self) -> List[dict]:
        """This method returns a list of unique pairs of country and city

        :returns: a list of dictionaries containing the country and city
        """
        offers = self.dao.get_all()

        locations = self._create_locations_list(offers)

        return locations

    @staticmethod
    def _create_locations_list(offers: List[Offer]) -> List[dict]:
        """This method creates a list of dictionaries containing the
        country and city from a list of offers

        :param offers: a list of Offer instances

        :returns: a list of dictionaries containing the country and city
        """
        locations = []

        for offer in offers:

            location = {offer.country: offer.city}

            if location not in locations:
                locations.append(location)

        return locations
