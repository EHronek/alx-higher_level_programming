#!/usr/bin/python3
''' takes in a URL, sends a request to the url
    and displays the value of the X-Request-Id variable in header
'''
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader("X-Request-Id")
        print(x_request_id)
