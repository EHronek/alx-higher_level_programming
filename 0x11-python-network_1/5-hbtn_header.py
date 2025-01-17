#!/usr/bin/python3
"""
takes in a url and sends a request to url
and display X-Request-Id in response header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    x_request_id = response.headers.get("X-Request-Id")

    if x_request_id:
        print(x_request_id)
