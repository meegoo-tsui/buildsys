#!/bin/sh

echo "save ..."
set -e

if [ $# != 1 ]; then
	CMD="patch.py -f build.ini -a 2"
	echo $CMD
	$CMD	
else
	CMD="patch.py -f build.ini -a 2 -o $1"
	echo $CMD
	$CMD
fi
echo "save success."

