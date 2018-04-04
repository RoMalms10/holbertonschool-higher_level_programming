#!/bin/bash
# Script that sends a POST request to a passed URL and displays the body
curl -sX POST "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
