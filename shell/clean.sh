#!/bin/sh

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
. $BUILD_SYS_PATH/shell/utils/base.sh
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
reset
# save then clean
if [ $# != 1 ]; then
	exec_cmd "patch.py -f build.ini -a 2"
	exec_cmd "patch.py -f build.ini -a 1"	
else
	exec_cmd "patch.py -f build.ini -a 2 -o $1"
	exec_cmd "patch.py -f build.ini -a 1 -o $1"
fi

