#!/usr/bin/python3
"""
sends a post request to url with letter as param
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    res = request.post(url, data={"q": q})

    try:
        js_data = res.json()
        if js_data:
            print(f"[{js_data.get('id')}] {js_data.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
