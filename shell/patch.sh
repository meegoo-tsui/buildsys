#!/bin/sh

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
. $BUILD_SYS_PATH/shell/utils/base.sh
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
reset
if [ $# != 1 ]; then
	exec_cmd "patch.py -f build.ini -a 0"	
else
	exec_cmd "patch.py -f build.ini -a 0 -o $1"
fi

