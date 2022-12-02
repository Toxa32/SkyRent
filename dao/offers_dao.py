"""This unit contains the OfferDAO class to get data from offers table"""
from typing import List

from dao.base import BaseDAO
from dao.models.offer import Offer
# -----------------------------------------------------------------------


class OfferDAO(BaseDAO[Offer]):
    """The OfferDAO class contains all necessary methods to get data
    from offers table"""
    __model__ = Offer

    def get_all(self, start_price: int = 0, end_price: int = 100000,
                city: str = None, country: str = None) -> List[Offer]:
        """This method returns a list of models filtrated by parameters

        :param start_price: a price to search offers from
        :param end_price: a price to search offers to
        :param city: a city to search offers by
        :param country: a country to search offers by

        :return: a list of models
        """
        query = self.__model__.query.filter(self.__model__.price.between(
            start_price, end_price))

        if city:
            query = query.filter(self.__model__.city.ilike(f'%{city}%'))

        if country:
            query = query.filter(self.__model__.country.ilike(f'%{country}%'))

        return query.all()



