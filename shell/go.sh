#!/bin/sh

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
. $BUILD_SYS_PATH/shell/utils/base.sh
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
reset
export FASTBUILD="1"
set -e

if [ $# != 1 ]; then
	exec_cmd "build.py -m -i"
else
	if [ "$1" == "s" ]; then
		exec_cmd "save.sh"
		exec_cmd "build.py -m -i"
	else
		exec_cmd "build.py -m -i -o $1"
	fi
fi

