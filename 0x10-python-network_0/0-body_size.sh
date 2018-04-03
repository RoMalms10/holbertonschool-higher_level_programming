#!/bin/bash
# Script that curls a URL passed to it
curl -sI "$1" | grep "Content-Length:" | cut -d: -f2 | cut -d" " -f2
