#!/usr/bin/python3
"""
fetches from url with the requests module
"""

import requests

if __name__ == '__main__':
    response = requests.get('https://alx-intranet.hbtn.io/status')
    content = response.text

    print("Body response:")
    print("\t- type:", type(content))
    print('\t- content:', content)
