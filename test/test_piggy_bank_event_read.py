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

from firefly_iii_client.models.piggy_bank_event_read import PiggyBankEventRead

class TestPiggyBankEventRead(unittest.TestCase):
    """PiggyBankEventRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PiggyBankEventRead:
        """Test PiggyBankEventRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PiggyBankEventRead`
        """
        model = PiggyBankEventRead()
        if include_optional:
            return PiggyBankEventRead(
                attributes = firefly_iii_client.models.piggy_bank_event.PiggyBankEvent(
                    amount = '123.45', 
                    created_at = '2018-09-17T12:46:47+01:00', 
                    currency_code = 'EUR', 
                    currency_decimal_places = 2, 
                    currency_id = '5', 
                    currency_symbol = '$', 
                    transaction_group_id = '4291', 
                    transaction_journal_id = '4291', 
                    updated_at = '2018-09-17T12:46:47+01:00', ),
                id = '2',
                links = firefly_iii_client.models.object_link.ObjectLink(
                    0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), 
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ),
                type = 'piggy_bank_events'
            )
        else:
            return PiggyBankEventRead(
                attributes = firefly_iii_client.models.piggy_bank_event.PiggyBankEvent(
                    amount = '123.45', 
                    created_at = '2018-09-17T12:46:47+01:00', 
                    currency_code = 'EUR', 
                    currency_decimal_places = 2, 
                    currency_id = '5', 
                    currency_symbol = '$', 
                    transaction_group_id = '4291', 
                    transaction_journal_id = '4291', 
                    updated_at = '2018-09-17T12:46:47+01:00', ),
                id = '2',
                links = firefly_iii_client.models.object_link.ObjectLink(
                    0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), 
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ),
                type = 'piggy_bank_events',
        )
        """

    def testPiggyBankEventRead(self):
        """Test PiggyBankEventRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
