#!/bin/bash
# displays all http methods the server will accept
curl -sI "$1" | grep "ALLOW" | cut -d " " -f 2-
