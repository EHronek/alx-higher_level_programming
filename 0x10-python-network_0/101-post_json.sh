#!/bin/bash
# sends a JSON post request to a url passed as the first arg and displays the body of the response
curl -s --request POST "$1" --data @"$2" -H "Content-Type: application/json"
