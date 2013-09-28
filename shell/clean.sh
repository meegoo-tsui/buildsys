#!/bin/sh

echo "clear ..."
set -e

# save then clean
if [ $# != 1 ]; then
	CMD="patch.py -f build.ini -a 2"
	CMD="patch.py -f build.ini -a 1"
	echo $CMD
	$CMD	
else
	CMD="patch.py -f build.ini -a 2 -o $1"
	CMD="patch.py -f build.ini -a 1 -o $1"
	echo $CMD
	$CMD
fi
echo "clear success."

