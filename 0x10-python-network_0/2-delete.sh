#!/bin/bash
# sends a DELETE request to the URL passed as the first arg and displays response body.
curl -s "$1" -X DELETE route_3
