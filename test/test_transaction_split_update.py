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

from firefly_iii_client.models.transaction_split_update import TransactionSplitUpdate

class TestTransactionSplitUpdate(unittest.TestCase):
    """TransactionSplitUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionSplitUpdate:
        """Test TransactionSplitUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionSplitUpdate`
        """
        model = TransactionSplitUpdate()
        if include_optional:
            return TransactionSplitUpdate(
                amount = '123.45',
                bill_id = '111',
                bill_name = 'Monthly rent',
                book_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                budget_id = '4',
                budget_name = 'Groceries',
                bunq_payment_id = '',
                category_id = '43',
                category_name = 'Groceries',
                currency_code = 'EUR',
                currency_decimal_places = 2,
                currency_id = '12',
                currency_name = 'Euro',
                currency_symbol = '$',
                var_date = '2018-09-17T12:46:47+01:00',
                description = 'Vegetables',
                destination_iban = 'NL02ABNA0123456789',
                destination_id = '2',
                destination_name = 'Buy and Large',
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                external_id = '',
                external_url = '',
                foreign_amount = '123.45',
                foreign_currency_code = 'USD',
                foreign_currency_decimal_places = 2,
                foreign_currency_id = '17',
                foreign_currency_symbol = '$',
                interest_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                internal_reference = '',
                invoice_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                notes = 'Some example notes',
                order = 0,
                payment_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                process_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                reconciled = False,
                sepa_batch_id = '',
                sepa_cc = '',
                sepa_ci = '',
                sepa_country = '',
                sepa_ct_id = '',
                sepa_ct_op = '',
                sepa_db = '',
                sepa_ep = '',
                source_iban = 'NL02ABNA0123456789',
                source_id = '2',
                source_name = 'Checking account',
                tags = [
                    'Barbecue preparation'
                    ],
                transaction_journal_id = '123',
                type = 'withdrawal'
            )
        else:
            return TransactionSplitUpdate(
        )
        """

    def testTransactionSplitUpdate(self):
        """Test TransactionSplitUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
