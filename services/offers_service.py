"""This unit contains the OfferService class to work with offers table"""
from dao.offers_dao import OfferDAO, Offer
from services.base import BaseService
# -----------------------------------------------------------------------


class OfferService(BaseService[OfferDAO, Offer]):
    """The OfferService class provides business logic to work with user's
    requests regarding offers"""
    pass


