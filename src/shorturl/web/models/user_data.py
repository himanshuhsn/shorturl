# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from .base_model_ import Model
from .. import util


class UserData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, username: str=None, email: str=None):  # noqa: E501
        """UserData - a model defined in Swagger

        :param username: The username of this UserData.  # noqa: E501
        :type username: str
        :param email: The email of this UserData.  # noqa: E501
        :type email: str
        """
        self.swagger_types = {
            'username': str,
            'email': str
        }

        self.attribute_map = {
            'username': 'username',
            'email': 'email'
        }

        self._username = username
        self._email = email

    @classmethod
    def from_dict(cls, dikt) -> 'UserData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserData of this UserData.  # noqa: E501
        :rtype: UserData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this UserData.


        :return: The username of this UserData.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this UserData.


        :param username: The username of this UserData.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def email(self) -> str:
        """Gets the email of this UserData.


        :return: The email of this UserData.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this UserData.


        :param email: The email of this UserData.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email
