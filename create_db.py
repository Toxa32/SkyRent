"""This file serves to create a database from a JSON file"""
from flask import current_app
from configs import ConfigManager
from utils import create_app, create_database, db

config = ConfigManager().get_config()
with create_app(config).app_context():

    create_database(db, current_app.config['JSON_DB_DATA'])
