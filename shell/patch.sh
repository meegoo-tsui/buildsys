#!/bin/sh

echo "patch ..."
set -e

if [ $# != 1 ]; then
	CMD="patch.py -f build.ini -a 0"
	echo $CMD
	$CMD	
else
	CMD="patch.py -f build.ini -a 0 -o $1"
	echo $CMD
	$CMD
fi
echo "patch success."

