#!/bin/sh

# http://stackoverflow.com/questions/4767396/linux-command-how-to-find-only-text-files
# find . -type f -print0 | xargs -0 file | grep -P text | cut -d: -f1
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ $# != 1 ]; then
	print_color.sh -g "Usage:"
	print_color.sh -g "$0 string"
	exit 1
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
find . -type f -print0 | xargs -0 file | grep -P text | cut -d: -f1 | xargs grep $1
exit 0

