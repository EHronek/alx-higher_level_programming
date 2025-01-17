#!/usr/bin/python3
"""
Sends request to url and displays repsonse body
handles http errors by printing the error code
if status >= 400
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)

    if res.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(res.text)
