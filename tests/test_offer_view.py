"""This unit contains TestOfferViews class to test CBVs"""
# -------------------------------------------------------------------------


class TestOfferViews:
    """The TestOfferViews class provides methods to test CBVs"""

    def test_get_all(self, client_app, offer_keys):
        """This method serves to test the GET method for /offers/ route

        :param client_app: fixture containing an instance of Flask test client
        :param offer_keys: fixture containing a set of required keys
        """

        request = client_app.get('/offers/')
        assert request.status_code == 200, "Status code is not 200"
        data = request.json

        self._check_offer_list(data, offer_keys)

    def test_get_all_by_filters(self, client_app, offer_keys):
        """This method serves to test the GET method for routes like
        /offers/?start_price=300&end_price=500'

        :param client_app: fixture containing an instance of Flask test client
        :param offer_keys: fixture containing a set of required keys
        """
        request = client_app.get('/offers/?start_price=300&end_price=500')

        assert request.status_code == 200, "Status code is not 200"

        result = request.json
        self._check_offer_list(result, offer_keys)

        request = client_app.get('/offers/?country=germany&city=berlin')

        assert request.status_code == 200, "Status code is not 200"

        result = request.json
        self._check_offer_list(result, offer_keys)

    def test_get_one(self, client_app, offer_keys):
        """This method serves to test the GET method for /offers/3 route

        :param client_app: fixture containing an instance of Flask test client
        :param offer_keys: fixture containing a set of required keys
        """

        request = client_app.get('/offers/3')

        assert request.status_code == 200, "Status code is not 200"

        result = request.json

        self._check_each_offer(result, offer_keys)

    @staticmethod
    def _check_each_offer(record: dict, offer_keys):
        """The secondary method to check provided single record

        :param record: a dictionary containing data to check
        :param offer_keys: fixture containing a set of required keys
        """
        assert type(record) == dict
        assert offer_keys.issubset(set(record.keys()))

    def _check_offer_list(self, records: list, offer_keys):
        """The secondary method to check provided list of records

        :param records: a list containing data to check
        :param offer_keys: fixture containing a set of required keys
        """

        assert len(records) != 0
        assert type(records) == list

        for record in records:
            self._check_each_offer(record, offer_keys)
