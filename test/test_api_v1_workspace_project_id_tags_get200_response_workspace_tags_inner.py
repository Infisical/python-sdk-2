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

from infisicalapi_client.models.api_v1_workspace_project_id_tags_get200_response_workspace_tags_inner import ApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner  # noqa: E501

class TestApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner(unittest.TestCase):
    """ApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner:
        """Test ApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner`
        """
        model = ApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner()  # noqa: E501
        if include_optional:
            return ApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner(
                id = '',
                slug = '',
                color = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = '',
                project_id = '',
                created_by_actor_type = 'user'
            )
        else:
            return ApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner(
                id = '',
                slug = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                project_id = '',
        )
        """

    def testApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner(self):
        """Test ApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
