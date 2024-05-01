#!/bin/bash
# taskes in a s=url sends the body of the request and displays blah blah blah:wq
curl -s -X GET -w "%{http_code}" -o /dev/null "$1"

