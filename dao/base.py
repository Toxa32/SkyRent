"""This unit contains the BaseDAO class with base methods for all DAOs"""
from typing import TypeVar, Generic, List, Optional

from setup import db
from setup.db.base_model import Base
# -----------------------------------------------------------------------
T = TypeVar('T', bound=Base)
# -----------------------------------------------------------------------


class BaseDAO(Generic[T]):
    """The BaseDAO class is a basic class to be inherited"""
    __model__ = Base

    def __init__(self) -> None:
        """Initialization of the class"""
        self._db = db

    def get_all(self) -> List[T]:
        """This method returns a list of models found in the certain table

        :returns: a list of models
        """
        return self.__model__.query.all()

    def get_by_id(self, pk: int) -> Optional[T]:
        """This method returns a single model found in the certain table

        :param pk: the id of searching model

        :returns: a model with necessary data
        """
        return self.__model__.query.get(pk)
