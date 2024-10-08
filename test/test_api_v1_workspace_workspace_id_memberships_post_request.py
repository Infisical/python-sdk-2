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

from infisicalapi_client.models.api_v1_workspace_workspace_id_memberships_post_request import ApiV1WorkspaceWorkspaceIdMembershipsPostRequest  # noqa: E501

class TestApiV1WorkspaceWorkspaceIdMembershipsPostRequest(unittest.TestCase):
    """ApiV1WorkspaceWorkspaceIdMembershipsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1WorkspaceWorkspaceIdMembershipsPostRequest:
        """Test ApiV1WorkspaceWorkspaceIdMembershipsPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1WorkspaceWorkspaceIdMembershipsPostRequest`
        """
        model = ApiV1WorkspaceWorkspaceIdMembershipsPostRequest()  # noqa: E501
        if include_optional:
            return ApiV1WorkspaceWorkspaceIdMembershipsPostRequest(
                members = [
                    infisicalapi_client.models._api_v1_workspace__workspace_id__memberships_post_request_members_inner._api_v1_workspace__workspaceId__memberships_post_request_members_inner(
                        org_membership_id = '', 
                        workspace_encrypted_key = '', 
                        workspace_encrypted_nonce = '', )
                    ]
            )
        else:
            return ApiV1WorkspaceWorkspaceIdMembershipsPostRequest(
                members = [
                    infisicalapi_client.models._api_v1_workspace__workspace_id__memberships_post_request_members_inner._api_v1_workspace__workspaceId__memberships_post_request_members_inner(
                        org_membership_id = '', 
                        workspace_encrypted_key = '', 
                        workspace_encrypted_nonce = '', )
                    ],
        )
        """

    def testApiV1WorkspaceWorkspaceIdMembershipsPostRequest(self):
        """Test ApiV1WorkspaceWorkspaceIdMembershipsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
