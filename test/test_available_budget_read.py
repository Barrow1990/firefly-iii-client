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

from firefly_iii_client.models.available_budget_read import AvailableBudgetRead

class TestAvailableBudgetRead(unittest.TestCase):
    """AvailableBudgetRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AvailableBudgetRead:
        """Test AvailableBudgetRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AvailableBudgetRead`
        """
        model = AvailableBudgetRead()
        if include_optional:
            return AvailableBudgetRead(
                attributes = firefly_iii_client.models.available_budget.AvailableBudget(
                    amount = '123.45', 
                    created_at = '2018-09-17T12:46:47+01:00', 
                    currency_code = 'EUR', 
                    currency_decimal_places = 2, 
                    currency_id = '5', 
                    currency_symbol = '$', 
                    end = '2018-09-17T12:46:47+01:00', 
                    spent_in_budgets = [
                        firefly_iii_client.models.budget_spent.BudgetSpent(
                            currency_code = 'USD', 
                            currency_decimal_places = 2, 
                            currency_id = '5', 
                            currency_symbol = '$', 
                            sum = '123.45', )
                        ], 
                    spent_outside_budget = [
                        firefly_iii_client.models.budget_spent.BudgetSpent(
                            currency_code = 'USD', 
                            currency_decimal_places = 2, 
                            currency_id = '5', 
                            currency_symbol = '$', 
                            sum = '123.45', )
                        ], 
                    start = '2018-09-17T12:46:47+01:00', 
                    updated_at = '2018-09-17T12:46:47+01:00', ),
                id = '2',
                type = 'available_budgets'
            )
        else:
            return AvailableBudgetRead(
                attributes = firefly_iii_client.models.available_budget.AvailableBudget(
                    amount = '123.45', 
                    created_at = '2018-09-17T12:46:47+01:00', 
                    currency_code = 'EUR', 
                    currency_decimal_places = 2, 
                    currency_id = '5', 
                    currency_symbol = '$', 
                    end = '2018-09-17T12:46:47+01:00', 
                    spent_in_budgets = [
                        firefly_iii_client.models.budget_spent.BudgetSpent(
                            currency_code = 'USD', 
                            currency_decimal_places = 2, 
                            currency_id = '5', 
                            currency_symbol = '$', 
                            sum = '123.45', )
                        ], 
                    spent_outside_budget = [
                        firefly_iii_client.models.budget_spent.BudgetSpent(
                            currency_code = 'USD', 
                            currency_decimal_places = 2, 
                            currency_id = '5', 
                            currency_symbol = '$', 
                            sum = '123.45', )
                        ], 
                    start = '2018-09-17T12:46:47+01:00', 
                    updated_at = '2018-09-17T12:46:47+01:00', ),
                id = '2',
                type = 'available_budgets',
        )
        """

    def testAvailableBudgetRead(self):
        """Test AvailableBudgetRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
