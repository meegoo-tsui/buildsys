#!/bin/bash

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ $# != 1 ]; then
	print_color.sh -g "Usage:"
	print_color.sh -g "$0 file"
	exit 1
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
md="$1.md"
if [ ! -f $md ] ; then
	print_color.sh -r "No file - $md"
	exit 1
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
html="$1.html"
cmd="pandoc -s -S $md -o $html"
print_color.sh -g "$cmd"
$cmd
exit 0

