"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 1.5.4
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from firefly_iii_client.api_client import ApiClient, Endpoint as _Endpoint
from firefly_iii_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from firefly_iii_client.model.account_array import AccountArray
from firefly_iii_client.model.account_single import AccountSingle
from firefly_iii_client.model.account_store import AccountStore
from firefly_iii_client.model.account_type_filter import AccountTypeFilter
from firefly_iii_client.model.account_update import AccountUpdate
from firefly_iii_client.model.attachment_array import AttachmentArray
from firefly_iii_client.model.piggy_bank_array import PiggyBankArray
from firefly_iii_client.model.transaction_array import TransactionArray
from firefly_iii_client.model.transaction_type_filter import TransactionTypeFilter
from firefly_iii_client.model.validation_error import ValidationError


class AccountsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_account_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/accounts/{id}',
                'operation_id': 'delete_account',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (int,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_account_endpoint = _Endpoint(
            settings={
                'response_type': (AccountSingle,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/accounts/{id}',
                'operation_id': 'get_account',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'date',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (int,),
                    'date':
                        (date,),
                },
                'attribute_map': {
                    'id': 'id',
                    'date': 'date',
                },
                'location_map': {
                    'id': 'path',
                    'date': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_account_endpoint = _Endpoint(
            settings={
                'response_type': (AccountArray,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/accounts',
                'operation_id': 'list_account',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'date',
                    'type',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'date':
                        (date,),
                    'type':
                        (AccountTypeFilter,),
                },
                'attribute_map': {
                    'page': 'page',
                    'date': 'date',
                    'type': 'type',
                },
                'location_map': {
                    'page': 'query',
                    'date': 'query',
                    'type': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_attachment_by_account_endpoint = _Endpoint(
            settings={
                'response_type': (AttachmentArray,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/accounts/{id}/attachments',
                'operation_id': 'list_attachment_by_account',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'page',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (int,),
                    'page':
                        (int,),
                },
                'attribute_map': {
                    'id': 'id',
                    'page': 'page',
                },
                'location_map': {
                    'id': 'path',
                    'page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_piggy_bank_by_account_endpoint = _Endpoint(
            settings={
                'response_type': (PiggyBankArray,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/accounts/{id}/piggy_banks',
                'operation_id': 'list_piggy_bank_by_account',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'page',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (int,),
                    'page':
                        (int,),
                },
                'attribute_map': {
                    'id': 'id',
                    'page': 'page',
                },
                'location_map': {
                    'id': 'path',
                    'page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_transaction_by_account_endpoint = _Endpoint(
            settings={
                'response_type': (TransactionArray,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/accounts/{id}/transactions',
                'operation_id': 'list_transaction_by_account',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'page',
                    'limit',
                    'start',
                    'end',
                    'type',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (int,),
                    'page':
                        (int,),
                    'limit':
                        (int,),
                    'start':
                        (date,),
                    'end':
                        (date,),
                    'type':
                        (TransactionTypeFilter,),
                },
                'attribute_map': {
                    'id': 'id',
                    'page': 'page',
                    'limit': 'limit',
                    'start': 'start',
                    'end': 'end',
                    'type': 'type',
                },
                'location_map': {
                    'id': 'path',
                    'page': 'query',
                    'limit': 'query',
                    'start': 'query',
                    'end': 'query',
                    'type': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.store_account_endpoint = _Endpoint(
            settings={
                'response_type': (AccountSingle,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/accounts',
                'operation_id': 'store_account',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_store',
                ],
                'required': [
                    'account_store',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'account_store':
                        (AccountStore,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'account_store': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json',
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client
        )
        self.update_account_endpoint = _Endpoint(
            settings={
                'response_type': (AccountSingle,),
                'auth': [
                    'firefly_iii_auth'
                ],
                'endpoint_path': '/api/v1/accounts/{id}',
                'operation_id': 'update_account',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'account_update',
                ],
                'required': [
                    'id',
                    'account_update',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (int,),
                    'account_update':
                        (AccountUpdate,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                    'account_update': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json',
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client
        )

    def delete_account(
        self,
        id,
        **kwargs
    ):
        """Permanently delete account.  # noqa: E501

        Will permanently delete an account. Any associated transactions and piggy banks are ALSO deleted. Cannot be recovered from.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_account(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (int): The ID of the account.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.delete_account_endpoint.call_with_http_info(**kwargs)

    def get_account(
        self,
        id,
        **kwargs
    ):
        """Get single account.  # noqa: E501

        Returns a single account by its ID.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_account(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (int): The ID of the account.

        Keyword Args:
            date (date): A date formatted YYYY-MM-DD. When added to the request, Firefly III will show the account's balance on that day. . [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AccountSingle
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.get_account_endpoint.call_with_http_info(**kwargs)

    def list_account(
        self,
        **kwargs
    ):
        """List all accounts.  # noqa: E501

        This endpoint returns a list of all the accounts owned by the authenticated user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_account(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): Page number. The default pagination is per 50 items.. [optional]
            date (date): A date formatted YYYY-MM-DD. When added to the request, Firefly III will show the account's balance on that day. . [optional]
            type (AccountTypeFilter): Optional filter on the account type(s) returned. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AccountArray
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_account_endpoint.call_with_http_info(**kwargs)

    def list_attachment_by_account(
        self,
        id,
        **kwargs
    ):
        """Lists all attachments.  # noqa: E501

        Lists all attachments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_attachment_by_account(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (int): The ID of the account.

        Keyword Args:
            page (int): Page number. The default pagination is 50.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AttachmentArray
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.list_attachment_by_account_endpoint.call_with_http_info(**kwargs)

    def list_piggy_bank_by_account(
        self,
        id,
        **kwargs
    ):
        """List all piggy banks related to the account.  # noqa: E501

        This endpoint returns a list of all the piggy banks connected to the account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_piggy_bank_by_account(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (int): The ID of the account.

        Keyword Args:
            page (int): Page number. The default pagination is per 50 items.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PiggyBankArray
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.list_piggy_bank_by_account_endpoint.call_with_http_info(**kwargs)

    def list_transaction_by_account(
        self,
        id,
        **kwargs
    ):
        """List all transactions related to the account.  # noqa: E501

        This endpoint returns a list of all the transactions connected to the account.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_transaction_by_account(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (int): The ID of the account.

        Keyword Args:
            page (int): Page number. The default pagination is per 50 items.. [optional]
            limit (int): Limits the number of results on one page.. [optional]
            start (date): A date formatted YYYY-MM-DD. . [optional]
            end (date): A date formatted YYYY-MM-DD. . [optional]
            type (TransactionTypeFilter): Optional filter on the transaction type(s) returned.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            TransactionArray
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.list_transaction_by_account_endpoint.call_with_http_info(**kwargs)

    def store_account(
        self,
        account_store,
        **kwargs
    ):
        """Create new account.  # noqa: E501

        Creates a new account. The data required can be submitted as a JSON body or as a list of parameters (in key=value pairs, like a webform).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.store_account(account_store, async_req=True)
        >>> result = thread.get()

        Args:
            account_store (AccountStore): JSON array with the necessary account information or key=value pairs. See the model for the exact specifications.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AccountSingle
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['account_store'] = \
            account_store
        return self.store_account_endpoint.call_with_http_info(**kwargs)

    def update_account(
        self,
        id,
        account_update,
        **kwargs
    ):
        """Update existing account.  # noqa: E501

        Used to update a single account. All fields that are not submitted will be cleared (set to NULL). The model will tell you which fields are mandatory.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_account(id, account_update, async_req=True)
        >>> result = thread.get()

        Args:
            id (int): The ID of the account.
            account_update (AccountUpdate): JSON array or formdata with updated account information. See the model for the exact specifications.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AccountSingle
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        kwargs['account_update'] = \
            account_update
        return self.update_account_endpoint.call_with_http_info(**kwargs)

