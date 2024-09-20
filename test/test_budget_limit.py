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

from firefly_iii_client.models.budget_limit import BudgetLimit

class TestBudgetLimit(unittest.TestCase):
    """BudgetLimit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BudgetLimit:
        """Test BudgetLimit
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BudgetLimit`
        """
        model = BudgetLimit()
        if include_optional:
            return BudgetLimit(
                amount = '123.45',
                budget_id = '23',
                created_at = '2018-09-17T12:46:47+01:00',
                currency_code = 'EUR',
                currency_decimal_places = 2,
                currency_id = '5',
                currency_name = 'Euro',
                currency_symbol = '$',
                end = '2018-09-17T12:46:47+01:00',
                period = 'monthly',
                spent = '-1012.12',
                start = '2018-09-17T12:46:47+01:00',
                updated_at = '2018-09-17T12:46:47+01:00'
            )
        else:
            return BudgetLimit(
                amount = '123.45',
                budget_id = '23',
                end = '2018-09-17T12:46:47+01:00',
                start = '2018-09-17T12:46:47+01:00',
        )
        """

    def testBudgetLimit(self):
        """Test BudgetLimit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
