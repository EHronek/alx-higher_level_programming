#!/usr/bin/python3
"""Sends a post request to url with an email as param"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email})
    data = data.encode("utf-8")

    request = urllib.request.Request(url, data=data, method="POST")

    with urllib.request.urlopen(request) as response:
        response_data = response.read()
        response_data = response_data.decode("utf-8")
        print(response_data)
