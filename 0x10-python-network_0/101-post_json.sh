#!/bin/bash
# sends a JSON POST request to URL $1, and displays the response body
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"
