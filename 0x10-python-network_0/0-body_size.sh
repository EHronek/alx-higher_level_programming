#!/bin/bash
# Bash script that takes in aURL, sends a request to it and displays body size
curl -sI "$1" | grep "Content-Length" | awk '{print $2}'
