#!/bin/sh

echo "clear ..."
set -e

if [ $# != 1 ]; then
	CMD="patch.py -f build.ini -a 1"
	echo $CMD
	$CMD	
else
	CMD="patch.py -f build.ini -a 1 -o $1"
	echo $CMD
	$CMD
fi
echo "clear success."

