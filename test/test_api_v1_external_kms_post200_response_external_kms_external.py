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

from infisicalapi_client.models.api_v1_external_kms_post200_response_external_kms_external import ApiV1ExternalKmsPost200ResponseExternalKmsExternal  # noqa: E501

class TestApiV1ExternalKmsPost200ResponseExternalKmsExternal(unittest.TestCase):
    """ApiV1ExternalKmsPost200ResponseExternalKmsExternal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1ExternalKmsPost200ResponseExternalKmsExternal:
        """Test ApiV1ExternalKmsPost200ResponseExternalKmsExternal
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1ExternalKmsPost200ResponseExternalKmsExternal`
        """
        model = ApiV1ExternalKmsPost200ResponseExternalKmsExternal()  # noqa: E501
        if include_optional:
            return ApiV1ExternalKmsPost200ResponseExternalKmsExternal(
                id = '',
                status = '',
                status_details = '',
                provider = ''
            )
        else:
            return ApiV1ExternalKmsPost200ResponseExternalKmsExternal(
                id = '',
                provider = '',
        )
        """

    def testApiV1ExternalKmsPost200ResponseExternalKmsExternal(self):
        """Test ApiV1ExternalKmsPost200ResponseExternalKmsExternal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
