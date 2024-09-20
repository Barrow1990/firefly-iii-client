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

from firefly_iii_client.models.recurrence_single import RecurrenceSingle

class TestRecurrenceSingle(unittest.TestCase):
    """RecurrenceSingle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecurrenceSingle:
        """Test RecurrenceSingle
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecurrenceSingle`
        """
        model = RecurrenceSingle()
        if include_optional:
            return RecurrenceSingle(
                data = firefly_iii_client.models.recurrence_read.RecurrenceRead(
                    attributes = firefly_iii_client.models.recurrence.Recurrence(
                        active = True, 
                        apply_rules = True, 
                        created_at = '2018-09-17T12:46:47+01:00', 
                        description = 'Recurring transaction for the monthly rent', 
                        first_date = 'Mon Sep 17 00:00:00 UTC 2018', 
                        latest_date = 'Mon Sep 17 00:00:00 UTC 2018', 
                        notes = 'Some notes', 
                        nr_of_repetitions = 5, 
                        repeat_until = 'Mon Sep 17 00:00:00 UTC 2018', 
                        repetitions = [
                            firefly_iii_client.models.recurrence_repetition.RecurrenceRepetition(
                                created_at = '2018-09-17T12:46:47+01:00', 
                                description = 'Every week on Friday', 
                                id = '2', 
                                moment = '3', 
                                occurrences = [
                                    '2018-09-17T12:46:47+01:00'
                                    ], 
                                skip = 0, 
                                type = 'weekly', 
                                updated_at = '2018-09-17T12:46:47+01:00', 
                                weekend = 1, )
                            ], 
                        title = 'Rent', 
                        transactions = [
                            firefly_iii_client.models.recurrence_transaction.RecurrenceTransaction(
                                amount = '123.45', 
                                bill_id = '123', 
                                bill_name = '', 
                                budget_id = '4', 
                                budget_name = 'Groceries', 
                                category_id = '211', 
                                category_name = 'Bills', 
                                currency_code = 'EUR', 
                                currency_decimal_places = 2, 
                                currency_id = '3', 
                                currency_symbol = '€', 
                                description = 'Rent for the current month', 
                                destination_iban = 'NL02ABNA0123456789', 
                                destination_id = '258', 
                                destination_name = 'Buy and Large', 
                                destination_type = 'Asset account', 
                                foreign_amount = '123.45', 
                                foreign_currency_code = 'GBP', 
                                foreign_currency_decimal_places = 2, 
                                foreign_currency_id = '17', 
                                foreign_currency_symbol = '$', 
                                id = 'ID of the recurring transaction. Not to be confused with the ID of the recurrence itself.', 
                                piggy_bank_id = '123', 
                                piggy_bank_name = '', 
                                source_iban = 'NL02ABNA0123456789', 
                                source_id = '913', 
                                source_name = 'Checking account', 
                                source_type = 'Asset account', 
                                tags = [
                                    'Barbecue preparation'
                                    ], )
                            ], 
                        type = 'withdrawal', 
                        updated_at = '2018-09-17T12:46:47+01:00', ), 
                    id = '2', 
                    links = firefly_iii_client.models.object_link.ObjectLink(
                        0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                            rel = 'self', 
                            uri = '/OBJECTS/1', ), 
                        self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ), 
                    type = 'recurrences', )
            )
        else:
            return RecurrenceSingle(
                data = firefly_iii_client.models.recurrence_read.RecurrenceRead(
                    attributes = firefly_iii_client.models.recurrence.Recurrence(
                        active = True, 
                        apply_rules = True, 
                        created_at = '2018-09-17T12:46:47+01:00', 
                        description = 'Recurring transaction for the monthly rent', 
                        first_date = 'Mon Sep 17 00:00:00 UTC 2018', 
                        latest_date = 'Mon Sep 17 00:00:00 UTC 2018', 
                        notes = 'Some notes', 
                        nr_of_repetitions = 5, 
                        repeat_until = 'Mon Sep 17 00:00:00 UTC 2018', 
                        repetitions = [
                            firefly_iii_client.models.recurrence_repetition.RecurrenceRepetition(
                                created_at = '2018-09-17T12:46:47+01:00', 
                                description = 'Every week on Friday', 
                                id = '2', 
                                moment = '3', 
                                occurrences = [
                                    '2018-09-17T12:46:47+01:00'
                                    ], 
                                skip = 0, 
                                type = 'weekly', 
                                updated_at = '2018-09-17T12:46:47+01:00', 
                                weekend = 1, )
                            ], 
                        title = 'Rent', 
                        transactions = [
                            firefly_iii_client.models.recurrence_transaction.RecurrenceTransaction(
                                amount = '123.45', 
                                bill_id = '123', 
                                bill_name = '', 
                                budget_id = '4', 
                                budget_name = 'Groceries', 
                                category_id = '211', 
                                category_name = 'Bills', 
                                currency_code = 'EUR', 
                                currency_decimal_places = 2, 
                                currency_id = '3', 
                                currency_symbol = '€', 
                                description = 'Rent for the current month', 
                                destination_iban = 'NL02ABNA0123456789', 
                                destination_id = '258', 
                                destination_name = 'Buy and Large', 
                                destination_type = 'Asset account', 
                                foreign_amount = '123.45', 
                                foreign_currency_code = 'GBP', 
                                foreign_currency_decimal_places = 2, 
                                foreign_currency_id = '17', 
                                foreign_currency_symbol = '$', 
                                id = 'ID of the recurring transaction. Not to be confused with the ID of the recurrence itself.', 
                                piggy_bank_id = '123', 
                                piggy_bank_name = '', 
                                source_iban = 'NL02ABNA0123456789', 
                                source_id = '913', 
                                source_name = 'Checking account', 
                                source_type = 'Asset account', 
                                tags = [
                                    'Barbecue preparation'
                                    ], )
                            ], 
                        type = 'withdrawal', 
                        updated_at = '2018-09-17T12:46:47+01:00', ), 
                    id = '2', 
                    links = firefly_iii_client.models.object_link.ObjectLink(
                        0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                            rel = 'self', 
                            uri = '/OBJECTS/1', ), 
                        self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ), 
                    type = 'recurrences', ),
        )
        """

    def testRecurrenceSingle(self):
        """Test RecurrenceSingle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
