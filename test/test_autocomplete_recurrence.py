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

from firefly_iii_client.models.autocomplete_recurrence import AutocompleteRecurrence

class TestAutocompleteRecurrence(unittest.TestCase):
    """AutocompleteRecurrence unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AutocompleteRecurrence:
        """Test AutocompleteRecurrence
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AutocompleteRecurrence`
        """
        model = AutocompleteRecurrence()
        if include_optional:
            return AutocompleteRecurrence(
                description = 'Should trigger daily.',
                id = '2',
                name = 'Yearly bill'
            )
        else:
            return AutocompleteRecurrence(
                id = '2',
                name = 'Yearly bill',
        )
        """

    def testAutocompleteRecurrence(self):
        """Test AutocompleteRecurrence"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
