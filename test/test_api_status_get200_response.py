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

from infisicalapi_client.models.api_status_get200_response import ApiStatusGet200Response  # noqa: E501

class TestApiStatusGet200Response(unittest.TestCase):
    """ApiStatusGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiStatusGet200Response:
        """Test ApiStatusGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiStatusGet200Response`
        """
        model = ApiStatusGet200Response()  # noqa: E501
        if include_optional:
            return ApiStatusGet200Response(
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                message = 'Ok',
                email_configured = True,
                invite_only_signup = True,
                redis_configured = True,
                secret_scanning_configured = True,
                saml_default_org_slug = ''
            )
        else:
            return ApiStatusGet200Response(
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                message = 'Ok',
        )
        """

    def testApiStatusGet200Response(self):
        """Test ApiStatusGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
