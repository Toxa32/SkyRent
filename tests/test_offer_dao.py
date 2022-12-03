"""This unit contains TestOfferDao class to test OfferDAO"""
import pytest

# -------------------------------------------------------------------------


class TestOfferDao:
    """The TestOfferDao class provides methods to test OfferDAO"""

    def test_get_all(self, dao, app, offer_keys):
        """This method serves to test the get_all method of OfferDAO

        :param dao: fixture containing an instance of OfferDAO
        :param app: the application's fixture
        :param offer_keys: fixture containing a set of required keys
        """
        with app.app_context():
            result = dao.get_all()

            self._check_offer_list(result, offer_keys)

    def test_get_all_by_filters(self, dao, app, offer_keys):
        """This method serves to test the get_all method of OfferDAO with
        different filters

        :param dao: fixture containing an instance of OfferDAO
        :param app: the application's fixture
        :param offer_keys: fixture containing a set of required keys
        """

        with app.app_context():

            result = dao.get_all(start_price=300, end_price=500)
            self._check_offer_list(result, offer_keys)

            result = dao.get_all(country='germany', city='berlin')
            self._check_offer_list(result, offer_keys)

    def test_get_one(self, app, dao, offer_keys):
        """This method serves to test the get_by_id method of OfferDAO

        :param dao: fixture containing an instance of OfferDAO
        :param app: the application's fixture
        :param offer_keys: fixture containing a set of required keys
        """

        with app.app_context():
            result = dao.get_by_id(1)

        self._check_each_offer(result.__dict__, offer_keys)

    @staticmethod
    def _check_each_offer(record: dict, offer_keys):
        """The secondary method to check provided single record

        :param record: a dictionary containing data to check
        :param offer_keys: fixture containing a set of required keys
        """
        assert type(record) == dict, "The data's type is not dict"
        assert offer_keys.issubset(set(record.keys())), "The keys are wrong"

    def _check_offer_list(self, records: list, offer_keys):
        """The secondary method to check provided list of records

        :param records: a list containing data to check
        :param offer_keys: fixture containing a set of required keys
        """

        assert len(records) != 0, "The list of records is empty"
        assert type(records) == list, "The data's type is not list"

        for record in records:
            self._check_each_offer(record.__dict__, offer_keys)
