#!/bin/sh

find_cmd="find . -type d -empty"
print-color.sh -g "touch .gitignore in empty dirctory:"
eval $find_cmd

touch_cmd="$find_cmd -print0 | xargs -0 -I {} touch {}/.gitignore"
print-color.sh -g "command: $touch_cmd"
eval $touch_cmd

exit 0

