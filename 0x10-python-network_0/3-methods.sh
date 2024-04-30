#!/bin/bash
# taskes in a s=url sends the body of the request and displays blah blah blah:wq
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
