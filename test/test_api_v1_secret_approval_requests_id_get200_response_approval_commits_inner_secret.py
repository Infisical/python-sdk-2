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

from infisicalapi_client.models.api_v1_secret_approval_requests_id_get200_response_approval_commits_inner_secret import ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret  # noqa: E501

class TestApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret(unittest.TestCase):
    """ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret:
        """Test ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret`
        """
        model = ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret()  # noqa: E501
        if include_optional:
            return ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret(
                id = '',
                version = 1.337,
                secret_key = '',
                secret_value = '',
                secret_comment = ''
            )
        else:
            return ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret(
                id = '',
                version = 1.337,
                secret_key = '',
        )
        """

    def testApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret(self):
        """Test ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
