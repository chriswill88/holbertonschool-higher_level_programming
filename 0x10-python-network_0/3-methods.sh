#!/bin/bash
#This script display the methods from urls
curl -sI $1 | grep "Allow:" | cut -d ":" -f 2 | cut -c 2-
