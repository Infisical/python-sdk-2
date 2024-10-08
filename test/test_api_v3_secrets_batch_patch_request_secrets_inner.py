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

from infisicalapi_client.models.api_v3_secrets_batch_patch_request_secrets_inner import ApiV3SecretsBatchPatchRequestSecretsInner  # noqa: E501

class TestApiV3SecretsBatchPatchRequestSecretsInner(unittest.TestCase):
    """ApiV3SecretsBatchPatchRequestSecretsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3SecretsBatchPatchRequestSecretsInner:
        """Test ApiV3SecretsBatchPatchRequestSecretsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3SecretsBatchPatchRequestSecretsInner`
        """
        model = ApiV3SecretsBatchPatchRequestSecretsInner()  # noqa: E501
        if include_optional:
            return ApiV3SecretsBatchPatchRequestSecretsInner(
                secret_name = '',
                type = 'shared',
                secret_value_ciphertext = '',
                secret_value_iv = '',
                secret_value_tag = '',
                secret_key_ciphertext = '',
                secret_key_iv = '',
                secret_key_tag = '',
                secret_comment_ciphertext = '',
                secret_comment_iv = '',
                secret_comment_tag = '',
                skip_multiline_encoding = True,
                tags = [
                    ''
                    ]
            )
        else:
            return ApiV3SecretsBatchPatchRequestSecretsInner(
                secret_name = '',
                secret_value_ciphertext = '',
                secret_value_iv = '',
                secret_value_tag = '',
                secret_key_ciphertext = '',
                secret_key_iv = '',
                secret_key_tag = '',
        )
        """

    def testApiV3SecretsBatchPatchRequestSecretsInner(self):
        """Test ApiV3SecretsBatchPatchRequestSecretsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
