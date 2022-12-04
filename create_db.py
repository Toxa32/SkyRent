"""This file serves to create a database from a JSON file"""
import dotenv
from flask import current_app
from configs import ConfigManager
from utils import create_app, create_database, db
# ----------------------------------------------------------------------------
dotenv.load_dotenv()
config = ConfigManager().get_config()

with create_app(config).app_context():

    create_database(db, current_app.config['JSON_DB_DATA'])
