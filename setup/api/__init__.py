"""There is an Api instance in the unit for handy import to another
modules"""
from flask_restx import Api
# -------------------------------------------------------------------------

api = Api(version='1.0',
          title='SkyRent',
          description='Best real estate offers for you',
          doc='/doc'
          )
