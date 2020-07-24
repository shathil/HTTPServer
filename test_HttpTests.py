# mohqoue

from unittest import TestCase
from HttpTests import HTTPTest


class TestHTTP(TestCase):
    def setUp(self):

        request_block = "GET / HTTP/1.1"   # (method resource protocol)
        self.nhttp = HTTPTest(request_block.lower())


class TestHTTPTest(TestHTTP):

    def test_valid_request_size(self):
        self.assertEqual(len(self.nhttp.request.split(" ")), 3, "The request block length is not exactly three")

    def test_valid_request_block(self):
        self.assertTrue(self.nhttp.valid_request_block(), "at least one of the three elements of request is invalid")

    def test_is_method_valid(self):
        self.assertTrue(self.nhttp.is_method_valid(), "The method is invalid")

    def test_is_method_implemented(self):
        self.assertTrue(self.nhttp.is_method_implemented(), "The method is not implemented yet")

    def test_is_protocol_valid(self):
        self.assertTrue(self.nhttp.is_protocol_valid(), "The protocol is invalid")

    def test_is_protocol_implemented(self):
        self.assertTrue(self.nhttp.is_protocol_supported(), "The protocol is not implemented")

    def test_is_resource_available(self):
        self.assertTrue(self.nhttp.is_resource_available(), "The resource is not available")

    def test_is_response_code_200(self):
        res_http = "GET / HTTP/1.1"
        ok_http = HTTPTest(res_http.lower())
        self.assertEqual(ok_http.get_response_code(), 200, "The request is valid and the resource is found")

    def test_is_response_code_501_m(self):
        res_http = "PUT / HTTP/1.1"   # (method resource protocol)
        ni_http = HTTPTest(res_http.lower())
        self.assertEqual(ni_http.get_response_code(), 501, "The request method is not implemented")

    def test_is_response_code_501_p(self):
        res_http = "GET / HTTP/2.0"  # (method resource protocol)
        ni_http = HTTPTest(res_http.lower())
        self.assertEqual(ni_http.get_response_code(), 501, "The protocol is not implemented")

    def test_is_response_code_400_m(self):
        res_http = "GETT / HTTP/1.1"  # (method resource protocol)
        ok_http = HTTPTest(res_http.lower())
        self.assertEqual(ok_http.get_response_code(), 400, "The request method is invalid")

    def test_is_response_code_400_p(self):
        res_http = "GET / HTTP/11"  # (method resource protocol)
        ok_http = HTTPTest(res_http.lower())
        self.assertEqual(ok_http.get_response_code(), 400, "The protocol is invalid")

    def test_is_response_code_404(self):
        res_http = "GET //www.google.com HTTP/1.1"  # (method resource protocol)
        ok_http = HTTPTest(res_http.lower())
        self.assertEqual(ok_http.get_response_code(), 404, "The resource is not found is invalid")
