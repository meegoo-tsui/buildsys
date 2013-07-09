#!/bin/bash

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ $# != 1 ]; then
	print-color.sh -g "Usage:"
	print-color.sh -g "$0 file"
	exit 1
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
md="$1.md"
if [ ! -f $md ] ; then
	print-color.sh -r "No file - $md"
	exit 1
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
html="$1.html"
cmd="pandoc -s -S $md -o $html"
print-color.sh -g "$cmd"
$cmd
exit 0

