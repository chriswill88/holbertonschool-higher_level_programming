#!/bin/bash
# this script only displays url if status code of 200 is returned
if [ $(curl -X GET -I $1 -s | head -1 | cut -d " " -f 2) == 200 ]; then curl $1; else :; fi
