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

from infisicalapi_client.models.api_v1_access_approvals_requests_post200_response_approval import ApiV1AccessApprovalsRequestsPost200ResponseApproval  # noqa: E501

class TestApiV1AccessApprovalsRequestsPost200ResponseApproval(unittest.TestCase):
    """ApiV1AccessApprovalsRequestsPost200ResponseApproval unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AccessApprovalsRequestsPost200ResponseApproval:
        """Test ApiV1AccessApprovalsRequestsPost200ResponseApproval
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AccessApprovalsRequestsPost200ResponseApproval`
        """
        model = ApiV1AccessApprovalsRequestsPost200ResponseApproval()  # noqa: E501
        if include_optional:
            return ApiV1AccessApprovalsRequestsPost200ResponseApproval(
                id = '',
                policy_id = '',
                privilege_id = '',
                requested_by = '',
                is_temporary = True,
                temporary_range = '',
                permissions = None,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ApiV1AccessApprovalsRequestsPost200ResponseApproval(
                id = '',
                policy_id = '',
                requested_by = '',
                is_temporary = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testApiV1AccessApprovalsRequestsPost200ResponseApproval(self):
        """Test ApiV1AccessApprovalsRequestsPost200ResponseApproval"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
