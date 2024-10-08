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

from infisicalapi_client.models.api_v1_dynamic_secrets_leases_post_request import ApiV1DynamicSecretsLeasesPostRequest  # noqa: E501

class TestApiV1DynamicSecretsLeasesPostRequest(unittest.TestCase):
    """ApiV1DynamicSecretsLeasesPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1DynamicSecretsLeasesPostRequest:
        """Test ApiV1DynamicSecretsLeasesPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1DynamicSecretsLeasesPostRequest`
        """
        model = ApiV1DynamicSecretsLeasesPostRequest()  # noqa: E501
        if include_optional:
            return ApiV1DynamicSecretsLeasesPostRequest(
                dynamic_secret_name = '0',
                project_slug = '0',
                ttl = '',
                path = '/',
                environment_slug = '0'
            )
        else:
            return ApiV1DynamicSecretsLeasesPostRequest(
                dynamic_secret_name = '0',
                project_slug = '0',
                environment_slug = '0',
        )
        """

    def testApiV1DynamicSecretsLeasesPostRequest(self):
        """Test ApiV1DynamicSecretsLeasesPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
