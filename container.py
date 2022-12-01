"""This unit contains instances of DAOs and Services"""
from services.offers_service import OfferDAO, OfferService
# ------------------------------------------------------------------------

offer_dao = OfferDAO()

offers_service = OfferService(offer_dao)
