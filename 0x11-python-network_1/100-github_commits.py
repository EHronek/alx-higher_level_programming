#!/usr/bin/python3
"""
Takes 2 arguments Fetches the 10 most recent commits
GitHub repository.
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    repo = sys.argv[1]
    owner = sys.argv[2]

    res = requests.get(url, params={"per_page": 10})
    if res.status_code == 200:
        commits = res.json()
        for commit in commits:
            sha = commit.get("sha")
            author = commit.get("commit", {}).get("author", {}).get("name")
            print(f"{sha}: {author}")
    else:
        print(f"Error: Status Code: {res.status_code}")
