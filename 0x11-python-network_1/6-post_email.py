#!/usr/bin/python3
"""takes in a url and email address, sends a post request
to url with email as param and displays the body"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}

    response = requests.post(url, data=data)
    print(response)
