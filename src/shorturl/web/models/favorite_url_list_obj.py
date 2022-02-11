# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ..models.base_model_ import Model
from .. import util


class FavoriteUrlListObj(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, favorite_list: List[str]=None):  # noqa: E501
        """FavoriteUrlListObj - a model defined in Swagger

        :param favorite_list: The favorite_list of this FavoriteUrlListObj.  # noqa: E501
        :type favorite_list: List[str]
        """
        self.swagger_types = {
            'favorite_list': List[str]
        }

        self.attribute_map = {
            'favorite_list': 'favorite_list'
        }

        self._favorite_list = favorite_list

    @classmethod
    def from_dict(cls, dikt) -> 'FavoriteUrlListObj':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FavoriteUrlListObj of this FavoriteUrlListObj.  # noqa: E501
        :rtype: FavoriteUrlListObj
        """
        return util.deserialize_model(dikt, cls)

    @property
    def favorite_list(self) -> List[str]:
        """Gets the favorite_list of this FavoriteUrlListObj.


        :return: The favorite_list of this FavoriteUrlListObj.
        :rtype: List[str]
        """
        return self._favorite_list

    @favorite_list.setter
    def favorite_list(self, favorite_list: List[str]):
        """Sets the favorite_list of this FavoriteUrlListObj.


        :param favorite_list: The favorite_list of this FavoriteUrlListObj.
        :type favorite_list: List[str]
        """

        self._favorite_list = favorite_list
