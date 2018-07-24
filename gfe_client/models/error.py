# coding: utf-8

"""
    Allele Calling Service

    The Allele Calling  service provides an API for converting raw sequence data to GFE and HLA allele calls.  # noqa: E501

    OpenAPI spec version: 0.0.5
    Contact: mhalagan@nmdp.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Error(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'message': 'str',
        'pygfe_version': 'str',
        'gfedb_version': 'str',
        'imgtdb_version': 'str',
        'log': 'list[str]',
        'type': 'str'
    }

    attribute_map = {
        'message': 'Message',
        'pygfe_version': 'pygfe_version',
        'gfedb_version': 'gfedb_version',
        'imgtdb_version': 'imgtdb_version',
        'log': 'log',
        'type': 'type'
    }

    def __init__(self, message=None, pygfe_version=None, gfedb_version=None, imgtdb_version=None, log=None, type=None):  # noqa: E501
        """Error - a model defined in Swagger"""  # noqa: E501

        self._message = None
        self._pygfe_version = None
        self._gfedb_version = None
        self._imgtdb_version = None
        self._log = None
        self._type = None
        self.discriminator = None

        self.message = message
        self.pygfe_version = pygfe_version
        self.gfedb_version = gfedb_version
        self.imgtdb_version = imgtdb_version
        if log is not None:
            self.log = log
        if type is not None:
            self.type = type

    @property
    def message(self):
        """Gets the message of this Error.  # noqa: E501


        :return: The message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Error.


        :param message: The message of this Error.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def pygfe_version(self):
        """Gets the pygfe_version of this Error.  # noqa: E501


        :return: The pygfe_version of this Error.  # noqa: E501
        :rtype: str
        """
        return self._pygfe_version

    @pygfe_version.setter
    def pygfe_version(self, pygfe_version):
        """Sets the pygfe_version of this Error.


        :param pygfe_version: The pygfe_version of this Error.  # noqa: E501
        :type: str
        """
        if pygfe_version is None:
            raise ValueError("Invalid value for `pygfe_version`, must not be `None`")  # noqa: E501

        self._pygfe_version = pygfe_version

    @property
    def gfedb_version(self):
        """Gets the gfedb_version of this Error.  # noqa: E501


        :return: The gfedb_version of this Error.  # noqa: E501
        :rtype: str
        """
        return self._gfedb_version

    @gfedb_version.setter
    def gfedb_version(self, gfedb_version):
        """Sets the gfedb_version of this Error.


        :param gfedb_version: The gfedb_version of this Error.  # noqa: E501
        :type: str
        """
        if gfedb_version is None:
            raise ValueError("Invalid value for `gfedb_version`, must not be `None`")  # noqa: E501

        self._gfedb_version = gfedb_version

    @property
    def imgtdb_version(self):
        """Gets the imgtdb_version of this Error.  # noqa: E501


        :return: The imgtdb_version of this Error.  # noqa: E501
        :rtype: str
        """
        return self._imgtdb_version

    @imgtdb_version.setter
    def imgtdb_version(self, imgtdb_version):
        """Sets the imgtdb_version of this Error.


        :param imgtdb_version: The imgtdb_version of this Error.  # noqa: E501
        :type: str
        """
        if imgtdb_version is None:
            raise ValueError("Invalid value for `imgtdb_version`, must not be `None`")  # noqa: E501

        self._imgtdb_version = imgtdb_version

    @property
    def log(self):
        """Gets the log of this Error.  # noqa: E501


        :return: The log of this Error.  # noqa: E501
        :rtype: list[str]
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this Error.


        :param log: The log of this Error.  # noqa: E501
        :type: list[str]
        """

        self._log = log

    @property
    def type(self):
        """Gets the type of this Error.  # noqa: E501


        :return: The type of this Error.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Error.


        :param type: The type of this Error.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
