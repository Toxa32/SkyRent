"""This unit contains the OfferService class to work with offers table"""
from flask import abort

from dao.offers_dao import OfferDAO, Offer
from services.base import BaseService
from constants import METHODS
# -----------------------------------------------------------------------


class OfferService(BaseService[OfferDAO, Offer]):
    """The OfferService class provides business logic to work with user's
    requests regarding offers"""
    pass

    def get_all(self, **filters: dict):
        """This method returns a list of all offers filtrated filters
        if ones was provided

        :param filters: a kwargs dictionary with filters to get certain offers

        :returns: a list of models
        """

        # checking provided filters and data types
        for key, value in filters.items():

            if key in ('start_price', 'end_price'):

                try:
                    value = str(int(float(value)))

                except ValueError:
                    abort(400, 'Bad Request')

            # this function used to reduce the number of validation conditions
            exec(f"""if not value.{METHODS[key]}:
                abort(400, "Bad Request")
            """)

        offers = self.dao.get_all(**filters)

        if not offers:
            abort(400, 'Unfortunately We have no records You are looking for')

        return offers
