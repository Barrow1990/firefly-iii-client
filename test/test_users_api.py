# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: 2.1.0
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from firefly_iii_client.api.users_api import UsersApi


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UsersApi()

    def tearDown(self) -> None:
        pass

    def test_delete_user(self) -> None:
        """Test case for delete_user

        Delete a user.
        """
        pass

    def test_get_user(self) -> None:
        """Test case for get_user

        Get a single user.
        """
        pass

    def test_list_user(self) -> None:
        """Test case for list_user

        List all users.
        """
        pass

    def test_store_user(self) -> None:
        """Test case for store_user

        Store a new user
        """
        pass

    def test_update_user(self) -> None:
        """Test case for update_user

        Update an existing user's information.
        """
        pass


if __name__ == '__main__':
    unittest.main()
