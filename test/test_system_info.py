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

from firefly_iii_client.models.system_info import SystemInfo

class TestSystemInfo(unittest.TestCase):
    """SystemInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemInfo:
        """Test SystemInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemInfo`
        """
        model = SystemInfo()
        if include_optional:
            return SystemInfo(
                data = firefly_iii_client.models.system_info_data.SystemInfo_data(
                    api_version = '2.0.0-alpha.1', 
                    driver = 'mysql', 
                    os = 'Linux', 
                    php_version = '8.1.5', 
                    version = '5.8.0-alpha.1', )
            )
        else:
            return SystemInfo(
        )
        """

    def testSystemInfo(self):
        """Test SystemInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
