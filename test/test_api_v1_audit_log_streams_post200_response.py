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

from infisicalapi_client.models.api_v1_audit_log_streams_post200_response import ApiV1AuditLogStreamsPost200Response  # noqa: E501

class TestApiV1AuditLogStreamsPost200Response(unittest.TestCase):
    """ApiV1AuditLogStreamsPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AuditLogStreamsPost200Response:
        """Test ApiV1AuditLogStreamsPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AuditLogStreamsPost200Response`
        """
        model = ApiV1AuditLogStreamsPost200Response()  # noqa: E501
        if include_optional:
            return ApiV1AuditLogStreamsPost200Response(
                audit_log_stream = infisicalapi_client.models._api_v1_audit_log_streams_get_200_response_audit_log_streams_inner._api_v1_audit_log_streams_get_200_response_auditLogStreams_inner(
                    id = '', 
                    url = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return ApiV1AuditLogStreamsPost200Response(
                audit_log_stream = infisicalapi_client.models._api_v1_audit_log_streams_get_200_response_audit_log_streams_inner._api_v1_audit_log_streams_get_200_response_auditLogStreams_inner(
                    id = '', 
                    url = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
        )
        """

    def testApiV1AuditLogStreamsPost200Response(self):
        """Test ApiV1AuditLogStreamsPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
