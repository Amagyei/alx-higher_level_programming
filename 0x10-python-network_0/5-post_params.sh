#!/bin/bash
# taskes in a s=url sends the body of the request and displays blah blah blah:wq
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
