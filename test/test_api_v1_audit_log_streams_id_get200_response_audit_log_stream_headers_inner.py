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

from infisicalapi_client.models.api_v1_audit_log_streams_id_get200_response_audit_log_stream_headers_inner import ApiV1AuditLogStreamsIdGet200ResponseAuditLogStreamHeadersInner  # noqa: E501

class TestApiV1AuditLogStreamsIdGet200ResponseAuditLogStreamHeadersInner(unittest.TestCase):
    """ApiV1AuditLogStreamsIdGet200ResponseAuditLogStreamHeadersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AuditLogStreamsIdGet200ResponseAuditLogStreamHeadersInner:
        """Test ApiV1AuditLogStreamsIdGet200ResponseAuditLogStreamHeadersInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AuditLogStreamsIdGet200ResponseAuditLogStreamHeadersInner`
        """
        model = ApiV1AuditLogStreamsIdGet200ResponseAuditLogStreamHeadersInner()  # noqa: E501
        if include_optional:
            return ApiV1AuditLogStreamsIdGet200ResponseAuditLogStreamHeadersInner(
                key = '',
                value = ''
            )
        else:
            return ApiV1AuditLogStreamsIdGet200ResponseAuditLogStreamHeadersInner(
                key = '',
                value = '',
        )
        """

    def testApiV1AuditLogStreamsIdGet200ResponseAuditLogStreamHeadersInner(self):
        """Test ApiV1AuditLogStreamsIdGet200ResponseAuditLogStreamHeadersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
