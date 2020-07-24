import os


class HTTPTest:

    def __init__(self, uri):
        self.request = uri
        self.method = ""
        self.url = ""
        self.protocol = ""
        self.method_valid = False
        self.protocol_valid = False
        self.url_valid = False
        self.response_code = 0

    request_methods = {
        'get': True,
        'post': False,
        'put': False,
        'delete': False,
        'patch': False
    }
    http_version = {'http/1.1': True, 'http/2.0': False}

    resource_urls = {
        '/',
        '/hello.html',
        '/available.html'
    }

    fixed_response_headers = {
        'Server': 'Capuche/1.0',
        'Content-Type': 'text/html'
    }

    response_codes = {
        400: 'Bad Request',
        200: 'OK',
        404: 'Not Found',
        501: 'Not Implemented'
    }

    def valid_request_block(self):
        parts = self.request.split(" ")
        if len(parts) != 3:
            return False
        if self.is_method_valid():
            self.method_valid = True
        if self.is_url_valid():
            self.url_valid = True
        if self.is_protocol_valid():
            self.protocol_valid = True
        if self.method_valid & self.protocol_valid:
            self.protocol = parts[2]
            self.method = parts[0]
            return True

    def is_method_valid(self):
        parts = self.request.split(" ")
        if parts[0].strip() in self.request_methods:
            return True
        else:
            return False

    def is_protocol_valid(self):
        parts = self.request.split(" ")
        if parts[2].strip() in self.http_version:
            return True
        else:
            return False

    def is_url_valid(self):
        parts = self.request.split(" ")
        if parts[1].strip() in self.resource_urls:
            return True
        else:
            return False

    def is_method_implemented(self):
        if self.valid_request_block():
            return self.request_methods[self.method]

    def is_protocol_supported(self):
        if self.valid_request_block():
            return self.http_version[self.protocol]

    def is_resource_available(self):
        # Not found
        if self.valid_request_block() & self.url_valid:
            return True
        else:
            return False

    def get_response_code(self):

        if not self.valid_request_block():
            code = 400
        elif not self.is_resource_available():
            code = 404
        elif (not self.is_method_implemented()) | (not self.is_protocol_supported()):
            code = 501
        elif self.is_resource_available():
            code = 200

        #response = self.get_response_text(code)
        return code

    def get_response(self, code):
        reason = self.response_codes[code]
        response_header = "%s %s %s\r\n" % (self.protocol, code, reason)
        headers = ""
        for header in self.fixed_response_headers:
            headers += "%s: %s \r\n" % (header, self.fixed_response_headers[header])

        body = self.get_response_body(code)
        headers += "Content-Length: %s \r\n" % (len(body))
        headers += "\r\n"
        response_header += headers
        return response_header + body

    def get_response_body(self, code):
        bodies = {
            200: '<html> <body> <h1>Request received!</h1> </body></html>',
            400: '<html> <body> <h1>Bad Request </h1> </body></html>',
            404: '<html> <body> <h1>The resource is not found </h1> </body></html>',
            501: '<html> <body> <h1>Request is not Implemented!</h1> </body></html>',
        }
        return bodies.get(code)
