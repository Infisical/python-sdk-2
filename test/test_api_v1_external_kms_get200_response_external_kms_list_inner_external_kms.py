# coding: utf-8

"""
    Infisical API

    List of all available APIs that can be consumed

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from infisicalapi_client.models.api_v1_external_kms_get200_response_external_kms_list_inner_external_kms import ApiV1ExternalKmsGet200ResponseExternalKmsListInnerExternalKms  # noqa: E501

class TestApiV1ExternalKmsGet200ResponseExternalKmsListInnerExternalKms(unittest.TestCase):
    """ApiV1ExternalKmsGet200ResponseExternalKmsListInnerExternalKms unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1ExternalKmsGet200ResponseExternalKmsListInnerExternalKms:
        """Test ApiV1ExternalKmsGet200ResponseExternalKmsListInnerExternalKms
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1ExternalKmsGet200ResponseExternalKmsListInnerExternalKms`
        """
        model = ApiV1ExternalKmsGet200ResponseExternalKmsListInnerExternalKms()  # noqa: E501
        if include_optional:
            return ApiV1ExternalKmsGet200ResponseExternalKmsListInnerExternalKms(
                provider = '',
                status = '',
                status_details = ''
            )
        else:
            return ApiV1ExternalKmsGet200ResponseExternalKmsListInnerExternalKms(
                provider = '',
        )
        """

    def testApiV1ExternalKmsGet200ResponseExternalKmsListInnerExternalKms(self):
        """Test ApiV1ExternalKmsGet200ResponseExternalKmsListInnerExternalKms"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
