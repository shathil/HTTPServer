#mohoque

The HTTPServer package contains four files. The main.py contains the main method which starts a TCP server for 127.0.0.1
and port 8080.

TCPServer is python class which implements the TCP severer. The server listens at port 8080 and spawns a thread
when it accepts a new connection. The thread implements non-blocking socket, reading the request at the socket
descriptor and writing the response to the socket descriptor.

The HTTPTest class implements the HTTP response for the HTTP request block. It supports five methods but
implements one method (GET). It supports HTTP/1.1 and HTTP/2.0, but implements HTTP/1.1. Three serving
resource routes are hardcoded.

test_HttpTests holds 13 unit tests for the HTTPTest class. The server was running on a MacBook Pro and accessible via the browsers; Chrome and Brave. It was also tested
with the command line tool called ‘curl’ .


The checklist
 
MUST requirements:
— Implementations language: Python (Yes)        
— Using of high level modules (BasicHTTPServer etc.) is not allowed (Yes)        
— The code must run on Linux (Runs on Mac)       
— Include configuration files, if required (No Config file, Configurations are hard coded as key-value
structures)      
— Minimal acceptable functionality: serving static content in response to GET requests (It implements GET
method and generates different reposes according to the request.)       
— Supports common web browsers (Firefox, Chrome…) (Checked with Chrome, Brave and Safari)         
— Unit-tests must be included (Included)         
— Focus on code testability, maintainability, stability, security, performance. (Adhered : Simplified APIs,
classes, client specific threads and message exchange happens in thread with non-blocking socket, resource
matching with the static resource list before accessing or executing should help to avoid some security issues)
 
