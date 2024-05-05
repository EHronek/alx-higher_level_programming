#!/bin/bash
# sends a request to url passed as an argurment and displays the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
