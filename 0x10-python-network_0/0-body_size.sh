#!/bin/bash
# this bash script takes in a url sends a request to it and then displays the size of its response
curl -I $1 -s | grep Content-Length: | cut -d " " -f 2
