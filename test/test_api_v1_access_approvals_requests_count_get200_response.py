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

from infisicalapi_client.models.api_v1_access_approvals_requests_count_get200_response import ApiV1AccessApprovalsRequestsCountGet200Response  # noqa: E501

class TestApiV1AccessApprovalsRequestsCountGet200Response(unittest.TestCase):
    """ApiV1AccessApprovalsRequestsCountGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AccessApprovalsRequestsCountGet200Response:
        """Test ApiV1AccessApprovalsRequestsCountGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AccessApprovalsRequestsCountGet200Response`
        """
        model = ApiV1AccessApprovalsRequestsCountGet200Response()  # noqa: E501
        if include_optional:
            return ApiV1AccessApprovalsRequestsCountGet200Response(
                pending_count = 1.337,
                finalized_count = 1.337
            )
        else:
            return ApiV1AccessApprovalsRequestsCountGet200Response(
                pending_count = 1.337,
                finalized_count = 1.337,
        )
        """

    def testApiV1AccessApprovalsRequestsCountGet200Response(self):
        """Test ApiV1AccessApprovalsRequestsCountGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
