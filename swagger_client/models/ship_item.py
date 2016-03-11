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


class ShipItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ShipItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'sk_us': 'list[str]',
            'ship_options': 'list[ShipOption]'
        }

        self.attribute_map = {
            'sk_us': 'SKUs',
            'ship_options': 'ShipOptions'
        }

        self._sk_us = None
        self._ship_options = None

    @property
    def sk_us(self):
        """
        Gets the sk_us of this ShipItem.


        :return: The sk_us of this ShipItem.
        :rtype: list[str]
        """
        return self._sk_us

    @sk_us.setter
    def sk_us(self, sk_us):
        """
        Sets the sk_us of this ShipItem.


        :param sk_us: The sk_us of this ShipItem.
        :type: list[str]
        """
        self._sk_us = sk_us

    @property
    def ship_options(self):
        """
        Gets the ship_options of this ShipItem.


        :return: The ship_options of this ShipItem.
        :rtype: list[ShipOption]
        """
        return self._ship_options

    @ship_options.setter
    def ship_options(self, ship_options):
        """
        Sets the ship_options of this ShipItem.


        :param ship_options: The ship_options of this ShipItem.
        :type: list[ShipOption]
        """
        self._ship_options = ship_options

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
