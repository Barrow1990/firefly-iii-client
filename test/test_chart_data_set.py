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

from firefly_iii_client.models.chart_data_set import ChartDataSet

class TestChartDataSet(unittest.TestCase):
    """ChartDataSet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChartDataSet:
        """Test ChartDataSet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChartDataSet`
        """
        model = ChartDataSet()
        if include_optional:
            return ChartDataSet(
                currency_code = 'EUR',
                currency_decimal_places = 2,
                currency_id = '5',
                currency_symbol = '$',
                end_date = '2018-09-17T12:46:47+01:00',
                entries = [
                    firefly_iii_client.models.chart_data_point.ChartDataPoint(
                        key = 'value', )
                    ],
                label = 'Checking account',
                start_date = '2018-09-17T12:46:47+01:00',
                type = 'line',
                y_axis_id = 0
            )
        else:
            return ChartDataSet(
        )
        """

    def testChartDataSet(self):
        """Test ChartDataSet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
