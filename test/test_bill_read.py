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

from firefly_iii_client.models.bill_read import BillRead

class TestBillRead(unittest.TestCase):
    """BillRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillRead:
        """Test BillRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillRead`
        """
        model = BillRead()
        if include_optional:
            return BillRead(
                attributes = firefly_iii_client.models.bill.Bill(
                    active = True, 
                    amount_max = '123.45', 
                    amount_min = '123.45', 
                    created_at = '2018-09-17T12:46:47+01:00', 
                    currency_code = 'EUR', 
                    currency_decimal_places = 2, 
                    currency_id = '5', 
                    currency_symbol = '$', 
                    date = '2018-09-17T12:46:47+01:00', 
                    end_date = '2018-09-17T12:46:47+01:00', 
                    extension_date = '2018-09-17T12:46:47+01:00', 
                    name = 'Rent', 
                    next_expected_match = '2018-09-17T12:46:47+01:00', 
                    next_expected_match_diff = 'today', 
                    notes = 'Some example notes', 
                    object_group_id = '5', 
                    object_group_order = 5, 
                    object_group_title = 'Example Group', 
                    order = 1, 
                    paid_dates = [
                        firefly_iii_client.models.bill_paid_dates_inner.Bill_paid_dates_inner(
                            date = '2018-09-17T12:46:47+01:00', 
                            transaction_group_id = '123', 
                            transaction_journal_id = '123', )
                        ], 
                    pay_dates = [
                        '2018-09-17T12:46:47+01:00'
                        ], 
                    repeat_freq = 'monthly', 
                    skip = 0, 
                    updated_at = '2018-09-17T12:46:47+01:00', ),
                id = '2',
                type = 'bills'
            )
        else:
            return BillRead(
                attributes = firefly_iii_client.models.bill.Bill(
                    active = True, 
                    amount_max = '123.45', 
                    amount_min = '123.45', 
                    created_at = '2018-09-17T12:46:47+01:00', 
                    currency_code = 'EUR', 
                    currency_decimal_places = 2, 
                    currency_id = '5', 
                    currency_symbol = '$', 
                    date = '2018-09-17T12:46:47+01:00', 
                    end_date = '2018-09-17T12:46:47+01:00', 
                    extension_date = '2018-09-17T12:46:47+01:00', 
                    name = 'Rent', 
                    next_expected_match = '2018-09-17T12:46:47+01:00', 
                    next_expected_match_diff = 'today', 
                    notes = 'Some example notes', 
                    object_group_id = '5', 
                    object_group_order = 5, 
                    object_group_title = 'Example Group', 
                    order = 1, 
                    paid_dates = [
                        firefly_iii_client.models.bill_paid_dates_inner.Bill_paid_dates_inner(
                            date = '2018-09-17T12:46:47+01:00', 
                            transaction_group_id = '123', 
                            transaction_journal_id = '123', )
                        ], 
                    pay_dates = [
                        '2018-09-17T12:46:47+01:00'
                        ], 
                    repeat_freq = 'monthly', 
                    skip = 0, 
                    updated_at = '2018-09-17T12:46:47+01:00', ),
                id = '2',
                type = 'bills',
        )
        """

    def testBillRead(self):
        """Test BillRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
