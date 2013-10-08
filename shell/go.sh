#!/bin/sh

export FASTBUILD="1"
echo "go ..."
set -e

if [ $# != 1 ]; then
	build.py -m -i
else
	if [ "$1" == "s" ]; then
		save.sh
		build.py -m -i
	else
		build.py -m -i -o $1
	fi
fi
echo "go success."

