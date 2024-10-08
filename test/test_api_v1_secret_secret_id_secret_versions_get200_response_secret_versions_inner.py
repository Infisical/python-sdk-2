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

from infisicalapi_client.models.api_v1_secret_secret_id_secret_versions_get200_response_secret_versions_inner import ApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner  # noqa: E501

class TestApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner(unittest.TestCase):
    """ApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner:
        """Test ApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner`
        """
        model = ApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner()  # noqa: E501
        if include_optional:
            return ApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner(
                id = '',
                id = '',
                workspace = '',
                environment = '',
                version = 1.337,
                type = '',
                secret_key = '',
                secret_value = '',
                secret_comment = '',
                secret_reminder_note = '',
                secret_reminder_repeat_days = 1.337,
                skip_multiline_encoding = True,
                metadata = None,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner(
                id = '',
                id = '',
                workspace = '',
                environment = '',
                version = 1.337,
                type = '',
                secret_key = '',
                secret_value = '',
                secret_comment = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner(self):
        """Test ApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
