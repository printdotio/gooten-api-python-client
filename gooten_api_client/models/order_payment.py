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


class OrderPayment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        OrderPayment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'braintree_encrypted_cc_number': 'str',
            'braintree_encrypted_cc_exp_date': 'str',
            'braintree_encrypted_ccv': 'str',
            'braintree_payment_nonce': 'str',
            'partner_billing_key': 'str',
            'total': 'int',
            'currency_code': 'str'
        }

        self.attribute_map = {
            'braintree_encrypted_cc_number': 'BraintreeEncryptedCCNumber',
            'braintree_encrypted_cc_exp_date': 'BraintreeEncryptedCCExpDate',
            'braintree_encrypted_ccv': 'BraintreeEncryptedCCV',
            'braintree_payment_nonce': 'BraintreePaymentNonce',
            'partner_billing_key': 'PartnerBillingKey',
            'total': 'Total',
            'currency_code': 'CurrencyCode'
        }

        self._braintree_encrypted_cc_number = None
        self._braintree_encrypted_cc_exp_date = None
        self._braintree_encrypted_ccv = None
        self._braintree_payment_nonce = None
        self._partner_billing_key = None
        self._total = None
        self._currency_code = None

    @property
    def braintree_encrypted_cc_number(self):
        """
        Gets the braintree_encrypted_cc_number of this OrderPayment.


        :return: The braintree_encrypted_cc_number of this OrderPayment.
        :rtype: str
        """
        return self._braintree_encrypted_cc_number

    @braintree_encrypted_cc_number.setter
    def braintree_encrypted_cc_number(self, braintree_encrypted_cc_number):
        """
        Sets the braintree_encrypted_cc_number of this OrderPayment.


        :param braintree_encrypted_cc_number: The braintree_encrypted_cc_number of this OrderPayment.
        :type: str
        """
        self._braintree_encrypted_cc_number = braintree_encrypted_cc_number

    @property
    def braintree_encrypted_cc_exp_date(self):
        """
        Gets the braintree_encrypted_cc_exp_date of this OrderPayment.


        :return: The braintree_encrypted_cc_exp_date of this OrderPayment.
        :rtype: str
        """
        return self._braintree_encrypted_cc_exp_date

    @braintree_encrypted_cc_exp_date.setter
    def braintree_encrypted_cc_exp_date(self, braintree_encrypted_cc_exp_date):
        """
        Sets the braintree_encrypted_cc_exp_date of this OrderPayment.


        :param braintree_encrypted_cc_exp_date: The braintree_encrypted_cc_exp_date of this OrderPayment.
        :type: str
        """
        self._braintree_encrypted_cc_exp_date = braintree_encrypted_cc_exp_date

    @property
    def braintree_encrypted_ccv(self):
        """
        Gets the braintree_encrypted_ccv of this OrderPayment.


        :return: The braintree_encrypted_ccv of this OrderPayment.
        :rtype: str
        """
        return self._braintree_encrypted_ccv

    @braintree_encrypted_ccv.setter
    def braintree_encrypted_ccv(self, braintree_encrypted_ccv):
        """
        Sets the braintree_encrypted_ccv of this OrderPayment.


        :param braintree_encrypted_ccv: The braintree_encrypted_ccv of this OrderPayment.
        :type: str
        """
        self._braintree_encrypted_ccv = braintree_encrypted_ccv

    @property
    def braintree_payment_nonce(self):
        """
        Gets the braintree_payment_nonce of this OrderPayment.


        :return: The braintree_payment_nonce of this OrderPayment.
        :rtype: str
        """
        return self._braintree_payment_nonce

    @braintree_payment_nonce.setter
    def braintree_payment_nonce(self, braintree_payment_nonce):
        """
        Sets the braintree_payment_nonce of this OrderPayment.


        :param braintree_payment_nonce: The braintree_payment_nonce of this OrderPayment.
        :type: str
        """
        self._braintree_payment_nonce = braintree_payment_nonce

    @property
    def partner_billing_key(self):
        """
        Gets the partner_billing_key of this OrderPayment.
        A code that when passed allows the order to be submitted on credit.

        :return: The partner_billing_key of this OrderPayment.
        :rtype: str
        """
        return self._partner_billing_key

    @partner_billing_key.setter
    def partner_billing_key(self, partner_billing_key):
        """
        Sets the partner_billing_key of this OrderPayment.
        A code that when passed allows the order to be submitted on credit.

        :param partner_billing_key: The partner_billing_key of this OrderPayment.
        :type: str
        """
        self._partner_billing_key = partner_billing_key

    @property
    def total(self):
        """
        Gets the total of this OrderPayment.


        :return: The total of this OrderPayment.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this OrderPayment.


        :param total: The total of this OrderPayment.
        :type: int
        """
        self._total = total

    @property
    def currency_code(self):
        """
        Gets the currency_code of this OrderPayment.


        :return: The currency_code of this OrderPayment.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this OrderPayment.


        :param currency_code: The currency_code of this OrderPayment.
        :type: str
        """
        self._currency_code = currency_code

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

