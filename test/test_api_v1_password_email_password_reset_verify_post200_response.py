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

from infisicalapi_client.models.api_v1_password_email_password_reset_verify_post200_response import ApiV1PasswordEmailPasswordResetVerifyPost200Response  # noqa: E501

class TestApiV1PasswordEmailPasswordResetVerifyPost200Response(unittest.TestCase):
    """ApiV1PasswordEmailPasswordResetVerifyPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1PasswordEmailPasswordResetVerifyPost200Response:
        """Test ApiV1PasswordEmailPasswordResetVerifyPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1PasswordEmailPasswordResetVerifyPost200Response`
        """
        model = ApiV1PasswordEmailPasswordResetVerifyPost200Response()  # noqa: E501
        if include_optional:
            return ApiV1PasswordEmailPasswordResetVerifyPost200Response(
                message = '',
                user = infisicalapi_client.models._api_v1_password_email_password_reset_verify_post_200_response_user._api_v1_password_email_password_reset_verify_post_200_response_user(
                    id = '', 
                    email = '', 
                    auth_methods = [
                        ''
                        ], 
                    super_admin = True, 
                    first_name = '', 
                    last_name = '', 
                    is_accepted = True, 
                    is_mfa_enabled = True, 
                    mfa_methods = [
                        ''
                        ], 
                    devices = null, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    is_ghost = True, 
                    username = '', 
                    is_email_verified = True, 
                    consecutive_failed_mfa_attempts = 1.337, 
                    is_locked = True, 
                    temporary_lock_date_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    consecutive_failed_password_attempts = 1.337, ),
                token = ''
            )
        else:
            return ApiV1PasswordEmailPasswordResetVerifyPost200Response(
                message = '',
                user = infisicalapi_client.models._api_v1_password_email_password_reset_verify_post_200_response_user._api_v1_password_email_password_reset_verify_post_200_response_user(
                    id = '', 
                    email = '', 
                    auth_methods = [
                        ''
                        ], 
                    super_admin = True, 
                    first_name = '', 
                    last_name = '', 
                    is_accepted = True, 
                    is_mfa_enabled = True, 
                    mfa_methods = [
                        ''
                        ], 
                    devices = null, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    is_ghost = True, 
                    username = '', 
                    is_email_verified = True, 
                    consecutive_failed_mfa_attempts = 1.337, 
                    is_locked = True, 
                    temporary_lock_date_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    consecutive_failed_password_attempts = 1.337, ),
                token = '',
        )
        """

    def testApiV1PasswordEmailPasswordResetVerifyPost200Response(self):
        """Test ApiV1PasswordEmailPasswordResetVerifyPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
