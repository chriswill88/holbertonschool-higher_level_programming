#!/bin/bash
# this script send a post request to a url and displays the response
curl -s $1 -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
