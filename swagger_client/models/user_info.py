# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class UserInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UserInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'language_code': 'str',
            'country_code': 'str',
            'country_name': 'str',
            'currency_name': 'str',
            'currency_code': 'str',
            'currency_format': 'str'
        }

        self.attribute_map = {
            'language_code': 'LanguageCode',
            'country_code': 'CountryCode',
            'country_name': 'CountryName',
            'currency_name': 'CurrencyName',
            'currency_code': 'CurrencyCode',
            'currency_format': 'CurrencyFormat'
        }

        self._language_code = None
        self._country_code = None
        self._country_name = None
        self._currency_name = None
        self._currency_code = None
        self._currency_format = None

    @property
    def language_code(self):
        """
        Gets the language_code of this UserInfo.


        :return: The language_code of this UserInfo.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """
        Sets the language_code of this UserInfo.


        :param language_code: The language_code of this UserInfo.
        :type: str
        """
        self._language_code = language_code

    @property
    def country_code(self):
        """
        Gets the country_code of this UserInfo.


        :return: The country_code of this UserInfo.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this UserInfo.


        :param country_code: The country_code of this UserInfo.
        :type: str
        """
        self._country_code = country_code

    @property
    def country_name(self):
        """
        Gets the country_name of this UserInfo.


        :return: The country_name of this UserInfo.
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """
        Sets the country_name of this UserInfo.


        :param country_name: The country_name of this UserInfo.
        :type: str
        """
        self._country_name = country_name

    @property
    def currency_name(self):
        """
        Gets the currency_name of this UserInfo.


        :return: The currency_name of this UserInfo.
        :rtype: str
        """
        return self._currency_name

    @currency_name.setter
    def currency_name(self, currency_name):
        """
        Sets the currency_name of this UserInfo.


        :param currency_name: The currency_name of this UserInfo.
        :type: str
        """
        self._currency_name = currency_name

    @property
    def currency_code(self):
        """
        Gets the currency_code of this UserInfo.


        :return: The currency_code of this UserInfo.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this UserInfo.


        :param currency_code: The currency_code of this UserInfo.
        :type: str
        """
        self._currency_code = currency_code

    @property
    def currency_format(self):
        """
        Gets the currency_format of this UserInfo.


        :return: The currency_format of this UserInfo.
        :rtype: str
        """
        return self._currency_format

    @currency_format.setter
    def currency_format(self, currency_format):
        """
        Sets the currency_format of this UserInfo.


        :param currency_format: The currency_format of this UserInfo.
        :type: str
        """
        self._currency_format = currency_format

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
