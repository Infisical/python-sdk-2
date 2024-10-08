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

from infisicalapi_client.models.api_v1_organizations_organization_id_billing_details_patch_request import ApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest  # noqa: E501

class TestApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest(unittest.TestCase):
    """ApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest:
        """Test ApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest`
        """
        model = ApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest()  # noqa: E501
        if include_optional:
            return ApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest(
                email = '',
                name = ''
            )
        else:
            return ApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest(
        )
        """

    def testApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest(self):
        """Test ApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
