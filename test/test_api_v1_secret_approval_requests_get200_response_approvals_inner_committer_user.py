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

from infisicalapi_client.models.api_v1_secret_approval_requests_get200_response_approvals_inner_committer_user import ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser  # noqa: E501

class TestApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser(unittest.TestCase):
    """ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser:
        """Test ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser`
        """
        model = ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser()  # noqa: E501
        if include_optional:
            return ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser(
                user_id = '',
                email = '',
                first_name = '',
                last_name = '',
                username = ''
            )
        else:
            return ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser(
                user_id = '',
                username = '',
        )
        """

    def testApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser(self):
        """Test ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
