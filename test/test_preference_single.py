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

from firefly_iii_client.models.preference_single import PreferenceSingle

class TestPreferenceSingle(unittest.TestCase):
    """PreferenceSingle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PreferenceSingle:
        """Test PreferenceSingle
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PreferenceSingle`
        """
        model = PreferenceSingle()
        if include_optional:
            return PreferenceSingle(
                data = firefly_iii_client.models.preference_read.PreferenceRead(
                    attributes = firefly_iii_client.models.preference.Preference(
                        created_at = '2018-09-17T12:46:47+01:00', 
                        data = null, 
                        name = 'currencyPreference', 
                        updated_at = '2018-09-17T12:46:47+01:00', ), 
                    id = '2', 
                    type = 'preferences', )
            )
        else:
            return PreferenceSingle(
                data = firefly_iii_client.models.preference_read.PreferenceRead(
                    attributes = firefly_iii_client.models.preference.Preference(
                        created_at = '2018-09-17T12:46:47+01:00', 
                        data = null, 
                        name = 'currencyPreference', 
                        updated_at = '2018-09-17T12:46:47+01:00', ), 
                    id = '2', 
                    type = 'preferences', ),
        )
        """

    def testPreferenceSingle(self):
        """Test PreferenceSingle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
