#!/bin/bash
# displays all http methods the server will accept
curl -sI "$1" | grep Allow | cut -d ":" -f2| xargs
