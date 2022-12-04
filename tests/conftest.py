"""This unit contains fixtures for testing purposes"""
import os
import pytest
from configs import ConfigManager
from setup.db import db
from setup.api import api
from utils import create_database, create_app, add_namespaces
from dao.offers_dao import OfferDAO
from views.real_estate import real_estate_ns
from services.offers_service import OfferService
# --------------------------------------------------------------------------
os.environ['FLASK_MODE'] = 'test'
# --------------------------------------------------------------------------


@pytest.fixture(scope='session')
def app():
    """This function is fixture to create and return Flask application

    :return: a configured instance of Flask
    """
    app = create_app(ConfigManager().get_config())
    add_namespaces(api, [real_estate_ns])
    with app.app_context():

        create_database(db, app.config['JSON_DB_DATA'])

        return app


@pytest.fixture(scope='session')
def database():
    """This function is fixture to get SQLAlchemy instance

    :return: a SQLAlchemy instance
    """
    return db


@pytest.fixture(scope='session')
def client_app(app):
    """This function is fixture for test client

    :return: a test_client of Flask application
    """
    return app.test_client()


@pytest.fixture(scope='session')
def dao():
    """The fixture for OfferDAO

    :return: an instance of OfferDAO
    """
    return OfferDAO()


@pytest.fixture(scope='session')
def service(dao):
    """The fixture for OfferService

    :return: an instance of OfferService
    """
    return OfferService(dao)


@pytest.fixture(scope='session')
def offer_keys():
    """This function is a fixture returning a set of keys to validate
    the received data

    :return: a set of keys
    """

    keys = {
        "title",
        "id",
        "description",
        "picture_url",
        "price",
        "country",
        "city",
        "features_on",
        "features_off",
        "host_name",
        "host_phone",
        "host_location"
    }
    return keys
