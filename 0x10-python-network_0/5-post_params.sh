#!/bin/bash
# sends a POST request to t he passed URL and displays the body of response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
