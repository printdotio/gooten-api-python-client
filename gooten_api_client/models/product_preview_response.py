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


class ProductPreviewResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProductPreviewResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'url': 'str',
            'had_error': 'bool',
            'error_message': 'str'
        }

        self.attribute_map = {
            'url': 'Url',
            'had_error': 'HadError',
            'error_message': 'ErrorMessage'
        }

        self._url = None
        self._had_error = None
        self._error_message = None

    @property
    def url(self):
        """
        Gets the url of this ProductPreviewResponse.


        :return: The url of this ProductPreviewResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this ProductPreviewResponse.


        :param url: The url of this ProductPreviewResponse.
        :type: str
        """
        self._url = url

    @property
    def had_error(self):
        """
        Gets the had_error of this ProductPreviewResponse.


        :return: The had_error of this ProductPreviewResponse.
        :rtype: bool
        """
        return self._had_error

    @had_error.setter
    def had_error(self, had_error):
        """
        Sets the had_error of this ProductPreviewResponse.


        :param had_error: The had_error of this ProductPreviewResponse.
        :type: bool
        """
        self._had_error = had_error

    @property
    def error_message(self):
        """
        Gets the error_message of this ProductPreviewResponse.


        :return: The error_message of this ProductPreviewResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this ProductPreviewResponse.


        :param error_message: The error_message of this ProductPreviewResponse.
        :type: str
        """
        self._error_message = error_message

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

