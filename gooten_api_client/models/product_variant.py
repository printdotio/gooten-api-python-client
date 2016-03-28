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


class ProductVariant(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProductVariant - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'sku': 'str',
            'max_images': 'int',
            'has_templates': 'bool',
            'options': 'list[ProductOption]',
            'price_info': 'ProductPriceInfo',
            'partner_price_info': 'ProductPriceInfo'
        }

        self.attribute_map = {
            'sku': 'Sku',
            'max_images': 'MaxImages',
            'has_templates': 'HasTemplates',
            'options': 'Options',
            'price_info': 'PriceInfo',
            'partner_price_info': 'PartnerPriceInfo'
        }

        self._sku = None
        self._max_images = None
        self._has_templates = None
        self._options = None
        self._price_info = None
        self._partner_price_info = None

    @property
    def sku(self):
        """
        Gets the sku of this ProductVariant.


        :return: The sku of this ProductVariant.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this ProductVariant.


        :param sku: The sku of this ProductVariant.
        :type: str
        """
        self._sku = sku

    @property
    def max_images(self):
        """
        Gets the max_images of this ProductVariant.


        :return: The max_images of this ProductVariant.
        :rtype: int
        """
        return self._max_images

    @max_images.setter
    def max_images(self, max_images):
        """
        Sets the max_images of this ProductVariant.


        :param max_images: The max_images of this ProductVariant.
        :type: int
        """
        self._max_images = max_images

    @property
    def has_templates(self):
        """
        Gets the has_templates of this ProductVariant.


        :return: The has_templates of this ProductVariant.
        :rtype: bool
        """
        return self._has_templates

    @has_templates.setter
    def has_templates(self, has_templates):
        """
        Sets the has_templates of this ProductVariant.


        :param has_templates: The has_templates of this ProductVariant.
        :type: bool
        """
        self._has_templates = has_templates

    @property
    def options(self):
        """
        Gets the options of this ProductVariant.


        :return: The options of this ProductVariant.
        :rtype: list[ProductOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this ProductVariant.


        :param options: The options of this ProductVariant.
        :type: list[ProductOption]
        """
        self._options = options

    @property
    def price_info(self):
        """
        Gets the price_info of this ProductVariant.


        :return: The price_info of this ProductVariant.
        :rtype: ProductPriceInfo
        """
        return self._price_info

    @price_info.setter
    def price_info(self, price_info):
        """
        Sets the price_info of this ProductVariant.


        :param price_info: The price_info of this ProductVariant.
        :type: ProductPriceInfo
        """
        self._price_info = price_info

    @property
    def partner_price_info(self):
        """
        Gets the partner_price_info of this ProductVariant.


        :return: The partner_price_info of this ProductVariant.
        :rtype: ProductPriceInfo
        """
        return self._partner_price_info

    @partner_price_info.setter
    def partner_price_info(self, partner_price_info):
        """
        Sets the partner_price_info of this ProductVariant.


        :param partner_price_info: The partner_price_info of this ProductVariant.
        :type: ProductPriceInfo
        """
        self._partner_price_info = partner_price_info

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

