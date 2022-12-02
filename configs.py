"""This file contains configuration classes for different purposes like
development, testing and production"""
from pathlib import Path
from os import getenv
import dotenv
# ------------------------------------------------------------------------
dotenv.load_dotenv()
# ------------------------------------------------------------------------


class BaseConfig:
    """The BaseConfig class contains basic settings for application"""
    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False}
    BASE_DIR = Path(__file__).resolve().parent
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_DB_DATA = 'data.json'


class TestConfig(BaseConfig):
    """The TestConfig class contains settings to test application"""
    SQLALCHEMY_DATABASE_URI = f'sqlite:///:memory:'
    DEBUG = True


class DevelopConfig(BaseConfig):
    """The DevelopConfig class contains settings for development purposes"""
    DB_PATH = BaseConfig.BASE_DIR.joinpath('develop_db.db').as_posix()
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
    DEBUG = True


class ProductionConfig(BaseConfig):
    """The ProductionConfig class contains settings to start finished
    application"""
    DB_PATH = BaseConfig.BASE_DIR.joinpath('sky_rent.db').as_posix()
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
    DEBUG = False


class ConfigManager:
    """The ConfigManager class serves to receive configuration depending on
    environment variable 'FLASK_MODE'"""
    def __init__(self):

        self.env = getenv('FLASK_MODE')

    def get_config(self):

        if self.env == 'test':
            work_config = TestConfig()

        elif self.env == 'production':
            work_config = ProductionConfig()

        elif self.env == 'development':
            work_config = DevelopConfig()

        else:
            raise NotImplemented(f'Failed to get config for {self.env}')

        return work_config


