"""This unit contains functions to create and configure Flask application and
a database"""
import json

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from setup.db import db
from setup.api import api
from dao.models.offer import Offer
# -------------------------------------------------------------------------


def create_app(config) -> Flask:
    """This function creates an application

    :param config: Configuration class' instance

    :returns: configured application
    """
    app = Flask(__name__)
    app.config.from_object(config)
    create_extensions(app)
    return app


def create_extensions(app: Flask) -> None:
    """This function serves to configure Api and SQLAlchemy instances

    :param app: an instance of Flask
    """
    db.init_app(app)
    api.init_app(app)


def add_namespaces(api_obj: Api, namespaces: list) -> None:
    """This function serves to add namespaces in the API

    :param api_obj: an instance of Api
    :param namespaces: a list of namespaces
    """

    for namespace in namespaces:

        api_obj.add_namespace(namespace)


def create_database(db_obj: SQLAlchemy, filename: str) -> None:
    """This function serves to create a database

    :param db_obj: an instance of SQLAlchemy
    :param filename: a JSON file with necessary data
    """

    with db_obj.session.begin():

        db_obj.create_all()

        data = load_from_json(filename)

        add_data_to_database(data, db_obj)


def add_data_to_database(data: list, db_obj: SQLAlchemy) -> None:
    """This function serves to fill up a database by provided data

    :param data: a list of dictionaries
    :param db_obj: an instance of SQLAlchemy
    """
    for record in data:

        record['id'] = record.pop('pk')

        db_obj.session.add(Offer(**record))

    db_obj.session.commit()


def load_from_json(filename) -> list:
    """This function loads data from a JSON file

    :param filename: a JSON file

    :returns: deserialized JSON object
    """
    try:
        with open(filename, encoding='utf-8') as fin:

            return json.load(fin)

    except FileNotFoundError:
        print(f"File {filename} not found")

    except json.JSONDecodeError:
        print("Can't decode JSON")
