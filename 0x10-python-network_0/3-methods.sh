#!/bin/bash
# Script that dislpays all methods the server will accept
curl -Is "$1" | grep "Allow:" | cut -c 8-
