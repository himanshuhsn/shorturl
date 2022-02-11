# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ..models.base_model_ import Model
from .. import util


class MarkFavoriteObj(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, shorturl: str=None, markfavorite: str=None):  # noqa: E501
        """MarkFavoriteObj - a model defined in Swagger

        :param shorturl: The shorturl of this MarkFavoriteObj.  # noqa: E501
        :type shorturl: str
        :param markfavorite: The markfavorite of this MarkFavoriteObj.  # noqa: E501
        :type markfavorite: str
        """
        self.swagger_types = {
            'shorturl': str,
            'markfavorite': str
        }

        self.attribute_map = {
            'shorturl': 'shorturl',
            'markfavorite': 'markfavorite'
        }

        self._shorturl = shorturl
        self._markfavorite = markfavorite

    @classmethod
    def from_dict(cls, dikt) -> 'MarkFavoriteObj':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MarkFavoriteObj of this MarkFavoriteObj.  # noqa: E501
        :rtype: MarkFavoriteObj
        """
        return util.deserialize_model(dikt, cls)

    @property
    def shorturl(self) -> str:
        """Gets the shorturl of this MarkFavoriteObj.


        :return: The shorturl of this MarkFavoriteObj.
        :rtype: str
        """
        return self._shorturl

    @shorturl.setter
    def shorturl(self, shorturl: str):
        """Sets the shorturl of this MarkFavoriteObj.


        :param shorturl: The shorturl of this MarkFavoriteObj.
        :type shorturl: str
        """
        if shorturl is None:
            raise ValueError("Invalid value for `shorturl`, must not be `None`")  # noqa: E501

        self._shorturl = shorturl

    @property
    def markfavorite(self) -> str:
        """Gets the markfavorite of this MarkFavoriteObj.


        :return: The markfavorite of this MarkFavoriteObj.
        :rtype: str
        """
        return self._markfavorite

    @markfavorite.setter
    def markfavorite(self, markfavorite: str):
        """Sets the markfavorite of this MarkFavoriteObj.


        :param markfavorite: The markfavorite of this MarkFavoriteObj.
        :type markfavorite: str
        """
        if markfavorite is None:
            raise ValueError("Invalid value for `markfavorite`, must not be `None`")  # noqa: E501

        self._markfavorite = markfavorite
