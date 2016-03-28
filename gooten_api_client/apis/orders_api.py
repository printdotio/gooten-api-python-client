# coding: utf-8

"""
OrdersApi.py
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
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient



class OrdersApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client


    def g_et_orders(self, id, version, source, **kwargs):
        """
        Get an order
        Gets basic information about an order.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>

        >>> thread = api.g_et_orders(id, version, source, callback=callback_function)



        :param callback function: The callback function
            for asynchronous request. (optional)

        :param str id: Order Id (required)

        :param int version: Version of the api being used (required)

        :param str source: Description of the source-- ios, android, api (required)

        :param str language_code: Resultant info language. Defaults to 'en'.

        :return: PostSubmittedOrder
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'version', 'source', 'language_code']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_orders" % key
                )
            params[key] = val
        del params['kwargs']



        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `g_et_orders`")



        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `g_et_orders`")



        # verify the required parameter 'source' is set
        if ('source' not in params) or (params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `g_et_orders`")





        resource_path = '/v/{version}/source/{source}/orders/'.replace('{format}', 'json')
        path_params = {}

        if 'version' in params:
            path_params['version'] = params['version']

        if 'source' in params:
            path_params['source'] = params['source']


        query_params = {}

        if 'id' in params:
            query_params['id'] = params['id']

        if 'language_code' in params:
            query_params['languageCode'] = params['language_code']


        header_params = {}


        form_params = []
        local_var_files = {}


        body_params = None


        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PostSubmittedOrder',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response


    def p_ost_orders(self, order, version, source, **kwargs):
        """
        Submit an order
        Places an order into the system. An order can be submitted as PrePayment (in order to temporarily place an order and get an ID for Paypal) using the IsPreSubmit flag.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>

        >>> thread = api.p_ost_orders(order, version, source, callback=callback_function)



        :param callback function: The callback function
            for asynchronous request. (optional)

        :param PostOrder order: Order to be submitted (required)

        :param int version: Version of the api being used (required)

        :param str source: Description of the source-- ios, android, api (required)

        :return: OrderResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order', 'version', 'source']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_orders" % key
                )
            params[key] = val
        del params['kwargs']



        # verify the required parameter 'order' is set
        if ('order' not in params) or (params['order'] is None):
            raise ValueError("Missing the required parameter `order` when calling `p_ost_orders`")



        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `p_ost_orders`")



        # verify the required parameter 'source' is set
        if ('source' not in params) or (params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `p_ost_orders`")



        resource_path = '/v/{version}/source/{source}/orders/'.replace('{format}', 'json')
        path_params = {}

        if 'version' in params:
            path_params['version'] = params['version']

        if 'source' in params:
            path_params['source'] = params['source']


        query_params = {}


        header_params = {}


        form_params = []
        local_var_files = {}


        body_params = None

        if 'order' in params:
            body_params = params['order']


        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='OrderResult',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

