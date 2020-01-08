#!/bin/bash
# task 4 custom header sender
curl -si -X GET $1 -H "X-HolbertonSchool-User-Id: 98" | tail -n 1
