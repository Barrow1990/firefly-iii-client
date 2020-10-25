# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from firefly_iii_client.configuration import Configuration


class Transaction(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'apply_rules': 'bool',
        'created_at': 'datetime',
        'error_if_duplicate_hash': 'bool',
        'group_title': 'str',
        'transactions': 'list[TransactionSplit]',
        'updated_at': 'datetime',
        'user': 'int'
    }

    attribute_map = {
        'apply_rules': 'apply_rules',
        'created_at': 'created_at',
        'error_if_duplicate_hash': 'error_if_duplicate_hash',
        'group_title': 'group_title',
        'transactions': 'transactions',
        'updated_at': 'updated_at',
        'user': 'user'
    }

    def __init__(self, apply_rules=None, created_at=None, error_if_duplicate_hash=None, group_title=None, transactions=None, updated_at=None, user=None, local_vars_configuration=None):  # noqa: E501
        """Transaction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._apply_rules = None
        self._created_at = None
        self._error_if_duplicate_hash = None
        self._group_title = None
        self._transactions = None
        self._updated_at = None
        self._user = None
        self.discriminator = None

        if apply_rules is not None:
            self.apply_rules = apply_rules
        if created_at is not None:
            self.created_at = created_at
        if error_if_duplicate_hash is not None:
            self.error_if_duplicate_hash = error_if_duplicate_hash
        if group_title is not None:
            self.group_title = group_title
        self.transactions = transactions
        if updated_at is not None:
            self.updated_at = updated_at
        if user is not None:
            self.user = user

    @property
    def apply_rules(self):
        """Gets the apply_rules of this Transaction.  # noqa: E501

        Whether or not to apply rules when submitting transaction.  # noqa: E501

        :return: The apply_rules of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._apply_rules

    @apply_rules.setter
    def apply_rules(self, apply_rules):
        """Sets the apply_rules of this Transaction.

        Whether or not to apply rules when submitting transaction.  # noqa: E501

        :param apply_rules: The apply_rules of this Transaction.  # noqa: E501
        :type: bool
        """

        self._apply_rules = apply_rules

    @property
    def created_at(self):
        """Gets the created_at of this Transaction.  # noqa: E501


        :return: The created_at of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Transaction.


        :param created_at: The created_at of this Transaction.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def error_if_duplicate_hash(self):
        """Gets the error_if_duplicate_hash of this Transaction.  # noqa: E501

        Break if the submitted transaction exists already.  # noqa: E501

        :return: The error_if_duplicate_hash of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._error_if_duplicate_hash

    @error_if_duplicate_hash.setter
    def error_if_duplicate_hash(self, error_if_duplicate_hash):
        """Sets the error_if_duplicate_hash of this Transaction.

        Break if the submitted transaction exists already.  # noqa: E501

        :param error_if_duplicate_hash: The error_if_duplicate_hash of this Transaction.  # noqa: E501
        :type: bool
        """

        self._error_if_duplicate_hash = error_if_duplicate_hash

    @property
    def group_title(self):
        """Gets the group_title of this Transaction.  # noqa: E501

        Title of the transaction if it has been split in more than one piece. Empty otherwise.  # noqa: E501

        :return: The group_title of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._group_title

    @group_title.setter
    def group_title(self, group_title):
        """Sets the group_title of this Transaction.

        Title of the transaction if it has been split in more than one piece. Empty otherwise.  # noqa: E501

        :param group_title: The group_title of this Transaction.  # noqa: E501
        :type: str
        """

        self._group_title = group_title

    @property
    def transactions(self):
        """Gets the transactions of this Transaction.  # noqa: E501


        :return: The transactions of this Transaction.  # noqa: E501
        :rtype: list[TransactionSplit]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this Transaction.


        :param transactions: The transactions of this Transaction.  # noqa: E501
        :type: list[TransactionSplit]
        """
        if self.local_vars_configuration.client_side_validation and transactions is None:  # noqa: E501
            raise ValueError("Invalid value for `transactions`, must not be `None`")  # noqa: E501

        self._transactions = transactions

    @property
    def updated_at(self):
        """Gets the updated_at of this Transaction.  # noqa: E501


        :return: The updated_at of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Transaction.


        :param updated_at: The updated_at of this Transaction.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this Transaction.  # noqa: E501

        User ID  # noqa: E501

        :return: The user of this Transaction.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Transaction.

        User ID  # noqa: E501

        :param user: The user of this Transaction.  # noqa: E501
        :type: int
        """

        self._user = user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Transaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Transaction):
            return True

        return self.to_dict() != other.to_dict()
