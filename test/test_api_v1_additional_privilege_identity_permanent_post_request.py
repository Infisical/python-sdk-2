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

from infisicalapi_client.models.api_v1_additional_privilege_identity_permanent_post_request import ApiV1AdditionalPrivilegeIdentityPermanentPostRequest  # noqa: E501

class TestApiV1AdditionalPrivilegeIdentityPermanentPostRequest(unittest.TestCase):
    """ApiV1AdditionalPrivilegeIdentityPermanentPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AdditionalPrivilegeIdentityPermanentPostRequest:
        """Test ApiV1AdditionalPrivilegeIdentityPermanentPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AdditionalPrivilegeIdentityPermanentPostRequest`
        """
        model = ApiV1AdditionalPrivilegeIdentityPermanentPostRequest()  # noqa: E501
        if include_optional:
            return ApiV1AdditionalPrivilegeIdentityPermanentPostRequest(
                identity_id = '0',
                project_slug = '0',
                slug = '0',
                permissions = [
                    infisicalapi_client.models._api_v1_workspace__project_slug__roles_post_request_permissions_inner._api_v1_workspace__projectSlug__roles_post_request_permissions_inner(
                        action = 'read', 
                        subject = 'role', 
                        conditions = infisicalapi_client.models._api_v1_workspace__project_slug__roles_post_request_permissions_inner_conditions._api_v1_workspace__projectSlug__roles_post_request_permissions_inner_conditions(
                            environment = '', 
                            secret_path = infisicalapi_client.models._api_v1_workspace__project_slug__roles_post_request_permissions_inner_conditions_secret_path._api_v1_workspace__projectSlug__roles_post_request_permissions_inner_conditions_secretPath(
                                __glob = '0', ), ), )
                    ],
                privilege_permission = infisicalapi_client.models._api_v1_additional_privilege_identity_permanent_post_request_privilege_permission._api_v1_additional_privilege_identity_permanent_post_request_privilegePermission(
                    actions = [
                        'read'
                        ], 
                    subject = 'secrets', 
                    conditions = infisicalapi_client.models._api_v1_additional_privilege_identity_permanent_post_request_privilege_permission_conditions._api_v1_additional_privilege_identity_permanent_post_request_privilegePermission_conditions(
                        environment = '', 
                        secret_path = infisicalapi_client.models._api_v1_workspace__project_slug__roles_post_request_permissions_inner_conditions_secret_path._api_v1_workspace__projectSlug__roles_post_request_permissions_inner_conditions_secretPath(
                            __glob = '0', ), ), )
            )
        else:
            return ApiV1AdditionalPrivilegeIdentityPermanentPostRequest(
                identity_id = '0',
                project_slug = '0',
        )
        """

    def testApiV1AdditionalPrivilegeIdentityPermanentPostRequest(self):
        """Test ApiV1AdditionalPrivilegeIdentityPermanentPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
