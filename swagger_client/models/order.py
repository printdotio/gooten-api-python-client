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


class Order(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Order - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ship_to_address': 'ShipToAddress',
            'items': 'list[OrderItem]',
            'payment': 'Payment',
            'coupon_code': 'str'
        }

        self.attribute_map = {
            'ship_to_address': 'ShipToAddress',
            'items': 'Items',
            'payment': 'Payment',
            'coupon_code': 'CouponCode'
        }

        self._ship_to_address = None
        self._items = None
        self._payment = None
        self._coupon_code = None

    @property
    def ship_to_address(self):
        """
        Gets the ship_to_address of this Order.


        :return: The ship_to_address of this Order.
        :rtype: ShipToAddress
        """
        return self._ship_to_address

    @ship_to_address.setter
    def ship_to_address(self, ship_to_address):
        """
        Sets the ship_to_address of this Order.


        :param ship_to_address: The ship_to_address of this Order.
        :type: ShipToAddress
        """
        self._ship_to_address = ship_to_address

    @property
    def items(self):
        """
        Gets the items of this Order.


        :return: The items of this Order.
        :rtype: list[OrderItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this Order.


        :param items: The items of this Order.
        :type: list[OrderItem]
        """
        self._items = items

    @property
    def payment(self):
        """
        Gets the payment of this Order.


        :return: The payment of this Order.
        :rtype: Payment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """
        Sets the payment of this Order.


        :param payment: The payment of this Order.
        :type: Payment
        """
        self._payment = payment

    @property
    def coupon_code(self):
        """
        Gets the coupon_code of this Order.


        :return: The coupon_code of this Order.
        :rtype: str
        """
        return self._coupon_code

    @coupon_code.setter
    def coupon_code(self, coupon_code):
        """
        Sets the coupon_code of this Order.


        :param coupon_code: The coupon_code of this Order.
        :type: str
        """
        self._coupon_code = coupon_code

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
