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

from infisicalapi_client.models.api_v2_organizations_organization_id_memberships_membership_id_project_memberships_get200_response import ApiV2OrganizationsOrganizationIdMembershipsMembershipIdProjectMembershipsGet200Response  # noqa: E501

class TestApiV2OrganizationsOrganizationIdMembershipsMembershipIdProjectMembershipsGet200Response(unittest.TestCase):
    """ApiV2OrganizationsOrganizationIdMembershipsMembershipIdProjectMembershipsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2OrganizationsOrganizationIdMembershipsMembershipIdProjectMembershipsGet200Response:
        """Test ApiV2OrganizationsOrganizationIdMembershipsMembershipIdProjectMembershipsGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2OrganizationsOrganizationIdMembershipsMembershipIdProjectMembershipsGet200Response`
        """
        model = ApiV2OrganizationsOrganizationIdMembershipsMembershipIdProjectMembershipsGet200Response()  # noqa: E501
        if include_optional:
            return ApiV2OrganizationsOrganizationIdMembershipsMembershipIdProjectMembershipsGet200Response(
                memberships = [
                    infisicalapi_client.models._api_v1_workspace__workspace_id__users_get_200_response_users_inner._api_v1_workspace__workspaceId__users_get_200_response_users_inner(
                        id = '', 
                        user_id = '', 
                        project_id = '', 
                        user = infisicalapi_client.models._api_v1_workspace__workspace_id__users_get_200_response_users_inner_user._api_v1_workspace__workspaceId__users_get_200_response_users_inner_user(
                            email = '', 
                            username = '', 
                            first_name = '', 
                            last_name = '', 
                            id = '', 
                            public_key = '', ), 
                        project = infisicalapi_client.models._api_v1_workspace__workspace_id__users_get_200_response_users_inner_project._api_v1_workspace__workspaceId__users_get_200_response_users_inner_project(
                            name = '', 
                            id = '', ), 
                        roles = [
                            infisicalapi_client.models._api_v1_workspace__workspace_id__users_get_200_response_users_inner_roles_inner._api_v1_workspace__workspaceId__users_get_200_response_users_inner_roles_inner(
                                id = '', 
                                role = '', 
                                custom_role_id = '', 
                                custom_role_name = '', 
                                custom_role_slug = '', 
                                is_temporary = True, 
                                temporary_mode = '', 
                                temporary_range = '', 
                                temporary_access_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                temporary_access_end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], )
                    ]
            )
        else:
            return ApiV2OrganizationsOrganizationIdMembershipsMembershipIdProjectMembershipsGet200Response(
                memberships = [
                    infisicalapi_client.models._api_v1_workspace__workspace_id__users_get_200_response_users_inner._api_v1_workspace__workspaceId__users_get_200_response_users_inner(
                        id = '', 
                        user_id = '', 
                        project_id = '', 
                        user = infisicalapi_client.models._api_v1_workspace__workspace_id__users_get_200_response_users_inner_user._api_v1_workspace__workspaceId__users_get_200_response_users_inner_user(
                            email = '', 
                            username = '', 
                            first_name = '', 
                            last_name = '', 
                            id = '', 
                            public_key = '', ), 
                        project = infisicalapi_client.models._api_v1_workspace__workspace_id__users_get_200_response_users_inner_project._api_v1_workspace__workspaceId__users_get_200_response_users_inner_project(
                            name = '', 
                            id = '', ), 
                        roles = [
                            infisicalapi_client.models._api_v1_workspace__workspace_id__users_get_200_response_users_inner_roles_inner._api_v1_workspace__workspaceId__users_get_200_response_users_inner_roles_inner(
                                id = '', 
                                role = '', 
                                custom_role_id = '', 
                                custom_role_name = '', 
                                custom_role_slug = '', 
                                is_temporary = True, 
                                temporary_mode = '', 
                                temporary_range = '', 
                                temporary_access_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                temporary_access_end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], )
                    ],
        )
        """

    def testApiV2OrganizationsOrganizationIdMembershipsMembershipIdProjectMembershipsGet200Response(self):
        """Test ApiV2OrganizationsOrganizationIdMembershipsMembershipIdProjectMembershipsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
