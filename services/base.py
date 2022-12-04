"""This unit contains the BaseService class to be inherited"""
from typing import TypeVar, Generic, Optional, List
from flask import abort
from dao.base import BaseDAO
from setup.db.base_model import Base
# -------------------------------------------------------------------------
T = TypeVar('T', bound=BaseDAO)
M = TypeVar('M', bound=Base)
# -------------------------------------------------------------------------


class BaseService(Generic[T, M]):
    """The BaseService class provides base business logic"""
    def __init__(self, dao: Optional[T]) -> None:
        """The initialization of the BaseService

        :param dao: a DAO instance to get data from a database
        """
        self.dao: Optional[T] = dao

    def get_all(self) -> List[M]:
        """This method returns a list of all records

        :returns: a list of models
        """
        records = self.dao.get_all()

        if not records:
            abort(400, 'Unfortunately We have no records You are looking for')

        return records

    def get_one(self, pk: int) -> Optional[M]:
        """This method returns a record found by its id

        :param pk: the id of the searching record

        :returns: a list of models
        """

        record = self.dao.get_by_id(pk)

        if not record:
            abort(400, 'There is not a record with id you are looking for')

        return record
