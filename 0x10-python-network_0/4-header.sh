#!/bin/bash
# Script that displays the body of a response with header variables
var="X-HolbertonSchool-User-Id"
val="98"
curl -s "$1" -H "$var: $val"
