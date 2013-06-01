#!/bin/sh

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
help()
{
	print-color.sh -g "Usage:"
	print-color.sh -g "$0 -u"
	print-color.sh -g "  checkout and update local"
	print-color.sh -g "$0 -s"
	print-color.sh -g "  checkout and update mirror"
	print-color.sh -g "$0 -d"
	print-color.sh -g "  checkout and update mirror dev"
	exit 1
}

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ $# != 1 ]; then
	help
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ "$1" == "-u" ]; then
	check.py -f $WORKSPACE/local/gitosis-admin.git/davinci-all.ini -u
elif [ "$1" == "-s" ]; then
	check.py -f $WORKSPACE/local/gitosis-admin.git/davinci-all-mirror.ini -u
elif [ "$1" == "-d" ]; then
	check.py -f $WORKSPACE/local/gitosis-admin.git/davinci-dev-mirror.ini -u
else
	help
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

