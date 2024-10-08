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

from infisicalapi_client.models.api_v1_workspace_workspace_id_kms_patch_request_kms_any_of1 import ApiV1WorkspaceWorkspaceIdKmsPatchRequestKmsAnyOf1  # noqa: E501

class TestApiV1WorkspaceWorkspaceIdKmsPatchRequestKmsAnyOf1(unittest.TestCase):
    """ApiV1WorkspaceWorkspaceIdKmsPatchRequestKmsAnyOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1WorkspaceWorkspaceIdKmsPatchRequestKmsAnyOf1:
        """Test ApiV1WorkspaceWorkspaceIdKmsPatchRequestKmsAnyOf1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1WorkspaceWorkspaceIdKmsPatchRequestKmsAnyOf1`
        """
        model = ApiV1WorkspaceWorkspaceIdKmsPatchRequestKmsAnyOf1()  # noqa: E501
        if include_optional:
            return ApiV1WorkspaceWorkspaceIdKmsPatchRequestKmsAnyOf1(
                type = 'external',
                kms_id = ''
            )
        else:
            return ApiV1WorkspaceWorkspaceIdKmsPatchRequestKmsAnyOf1(
                type = 'external',
                kms_id = '',
        )
        """

    def testApiV1WorkspaceWorkspaceIdKmsPatchRequestKmsAnyOf1(self):
        """Test ApiV1WorkspaceWorkspaceIdKmsPatchRequestKmsAnyOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
