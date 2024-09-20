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

from firefly_iii_client.models.recurrence_update import RecurrenceUpdate

class TestRecurrenceUpdate(unittest.TestCase):
    """RecurrenceUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecurrenceUpdate:
        """Test RecurrenceUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecurrenceUpdate`
        """
        model = RecurrenceUpdate()
        if include_optional:
            return RecurrenceUpdate(
                active = True,
                apply_rules = True,
                description = 'Recurring transaction for the monthly rent',
                first_date = 'Mon Sep 17 00:00:00 UTC 2018',
                notes = 'Some notes',
                nr_of_repetitions = 5,
                repeat_until = 'Mon Sep 17 00:00:00 UTC 2018',
                repetitions = [
                    firefly_iii_client.models.recurrence_repetition_update.RecurrenceRepetitionUpdate(
                        moment = '3', 
                        skip = 0, 
                        type = 'weekly', 
                        weekend = 1, )
                    ],
                title = 'Rent',
                transactions = [
                    firefly_iii_client.models.recurrence_transaction_update.RecurrenceTransactionUpdate(
                        amount = '123.45', 
                        bill_id = '123', 
                        budget_id = '4', 
                        category_id = '211', 
                        currency_code = 'EUR', 
                        currency_id = '3', 
                        description = 'Rent for the current month', 
                        destination_id = '258', 
                        foreign_amount = '123.45', 
                        foreign_currency_id = '17', 
                        id = 'ID of the recurring transaction. Not to be confused with the ID of the recurrence itself. Is marked as REQUIRED but can be skipped when there is only ONE transaction.', 
                        piggy_bank_id = '123', 
                        source_id = '913', 
                        tags = [
                            'Barbecue preparation'
                            ], )
                    ]
            )
        else:
            return RecurrenceUpdate(
        )
        """

    def testRecurrenceUpdate(self):
        """Test RecurrenceUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
