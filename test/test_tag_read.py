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

from firefly_iii_client.models.tag_read import TagRead

class TestTagRead(unittest.TestCase):
    """TagRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TagRead:
        """Test TagRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TagRead`
        """
        model = TagRead()
        if include_optional:
            return TagRead(
                attributes = firefly_iii_client.models.a_single_tag_(c).A single tag (C)(
                    created_at = '2018-09-17T12:46:47+01:00', 
                    date = 'Mon Sep 17 00:00:00 UTC 2018', 
                    description = 'Tag for expensive stuff', 
                    latitude = 51.983333, 
                    longitude = 5.916667, 
                    tag = 'expensive', 
                    updated_at = '2018-09-17T12:46:47+01:00', 
                    zoom_level = 6, ),
                id = '2',
                links = firefly_iii_client.models.object_link.ObjectLink(
                    0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), 
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ),
                type = 'tags'
            )
        else:
            return TagRead(
                attributes = firefly_iii_client.models.a_single_tag_(c).A single tag (C)(
                    created_at = '2018-09-17T12:46:47+01:00', 
                    date = 'Mon Sep 17 00:00:00 UTC 2018', 
                    description = 'Tag for expensive stuff', 
                    latitude = 51.983333, 
                    longitude = 5.916667, 
                    tag = 'expensive', 
                    updated_at = '2018-09-17T12:46:47+01:00', 
                    zoom_level = 6, ),
                id = '2',
                links = firefly_iii_client.models.object_link.ObjectLink(
                    0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), 
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ),
                type = 'tags',
        )
        """

    def testTagRead(self):
        """Test TagRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
