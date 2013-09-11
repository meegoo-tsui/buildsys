#!/bin/sh

echo "save ..."
set -e

if [ $# != 1 ]; then
	CMD="patch.py -f backup.ini -a 2 -u"
	echo $CMD
	$CMD	
else
	CMD="patch.py -f backup.ini -a 2 -o -u $1"
	echo $CMD
	$CMD
fi
echo "save success."

