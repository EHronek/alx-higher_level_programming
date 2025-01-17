#!/usr/bin/python3
"""
Takes your github credentials and uses the gihub api display id
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    res = requests.get(url, auth=(username, token))
    data = res.json()
    print(data.get("id"))
