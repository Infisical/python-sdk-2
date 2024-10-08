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

from infisicalapi_client.models.api_v1_secret_approvals_post_request import ApiV1SecretApprovalsPostRequest  # noqa: E501

class TestApiV1SecretApprovalsPostRequest(unittest.TestCase):
    """ApiV1SecretApprovalsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretApprovalsPostRequest:
        """Test ApiV1SecretApprovalsPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretApprovalsPostRequest`
        """
        model = ApiV1SecretApprovalsPostRequest()  # noqa: E501
        if include_optional:
            return ApiV1SecretApprovalsPostRequest(
                workspace_id = '',
                name = '',
                environment = '',
                secret_path = '/',
                approvers = [
                    ''
                    ],
                approvals = 1,
                enforcement_level = 'hard'
            )
        else:
            return ApiV1SecretApprovalsPostRequest(
                workspace_id = '',
                environment = '',
                approvers = [
                    ''
                    ],
        )
        """

    def testApiV1SecretApprovalsPostRequest(self):
        """Test ApiV1SecretApprovalsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
