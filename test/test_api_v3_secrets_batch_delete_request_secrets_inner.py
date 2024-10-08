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

from infisicalapi_client.models.api_v3_secrets_batch_delete_request_secrets_inner import ApiV3SecretsBatchDeleteRequestSecretsInner  # noqa: E501

class TestApiV3SecretsBatchDeleteRequestSecretsInner(unittest.TestCase):
    """ApiV3SecretsBatchDeleteRequestSecretsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3SecretsBatchDeleteRequestSecretsInner:
        """Test ApiV3SecretsBatchDeleteRequestSecretsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3SecretsBatchDeleteRequestSecretsInner`
        """
        model = ApiV3SecretsBatchDeleteRequestSecretsInner()  # noqa: E501
        if include_optional:
            return ApiV3SecretsBatchDeleteRequestSecretsInner(
                secret_name = '',
                type = 'shared'
            )
        else:
            return ApiV3SecretsBatchDeleteRequestSecretsInner(
                secret_name = '',
        )
        """

    def testApiV3SecretsBatchDeleteRequestSecretsInner(self):
        """Test ApiV3SecretsBatchDeleteRequestSecretsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
