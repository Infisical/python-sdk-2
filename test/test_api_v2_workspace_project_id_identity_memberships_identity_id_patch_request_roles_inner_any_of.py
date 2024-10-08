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

from infisicalapi_client.models.api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_roles_inner_any_of import ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf  # noqa: E501

class TestApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf(unittest.TestCase):
    """ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf:
        """Test ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf`
        """
        model = ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf()  # noqa: E501
        if include_optional:
            return ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf(
                role = '',
                is_temporary = True
            )
        else:
            return ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf(
                role = '',
        )
        """

    def testApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf(self):
        """Test ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
