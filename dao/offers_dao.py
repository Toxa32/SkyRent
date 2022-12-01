"""This unit contains the OfferDAO class to get data from offers table"""
from dao.base import BaseDAO
from dao.models.offer import Offer
# -----------------------------------------------------------------------


class OfferDAO(BaseDAO[Offer]):
    """The OfferDAO class contains all necessary methods to get data
    from offers table"""
    __model__ = Offer
