#!/bin/bash
# makes a request to URL that causes server to respond with message containing "You got me!"
curl -sL --request PUT 0.0.0.0:5000/catch_me --data "user_id=98" -H "Origin:You got me!"
