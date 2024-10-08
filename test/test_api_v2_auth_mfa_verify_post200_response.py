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

from infisicalapi_client.models.api_v2_auth_mfa_verify_post200_response import ApiV2AuthMfaVerifyPost200Response  # noqa: E501

class TestApiV2AuthMfaVerifyPost200Response(unittest.TestCase):
    """ApiV2AuthMfaVerifyPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2AuthMfaVerifyPost200Response:
        """Test ApiV2AuthMfaVerifyPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2AuthMfaVerifyPost200Response`
        """
        model = ApiV2AuthMfaVerifyPost200Response()  # noqa: E501
        if include_optional:
            return ApiV2AuthMfaVerifyPost200Response(
                encryption_version = 1.337,
                protected_key = '',
                protected_key_iv = '',
                protected_key_tag = '',
                public_key = '',
                encrypted_private_key = '',
                iv = '',
                tag = '',
                token = ''
            )
        else:
            return ApiV2AuthMfaVerifyPost200Response(
                protected_key = '',
                protected_key_iv = '',
                protected_key_tag = '',
                public_key = '',
                encrypted_private_key = '',
                iv = '',
                tag = '',
                token = '',
        )
        """

    def testApiV2AuthMfaVerifyPost200Response(self):
        """Test ApiV2AuthMfaVerifyPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
