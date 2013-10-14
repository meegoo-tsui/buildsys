#!/bin/sh

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
. $BUILD_SYS_PATH/shell/utils/sdk.sh
. $BUILD_SYS_PATH/shell/utils/base.sh
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ $# == 0 ]; then
	print-color.sh -g "Usage:"
	print-color.sh -g "$0 server"
	exit 1
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ $# != 1 ] && [ "$2" == "all" ]; then
	old_sdk=`echo ${!keyword}`
	for (( i=0; i<len; i++ ))
		do 
			exec_cmd "export ${keyword}=${sdk[$i]}"
			exec_cmd "upload.py -f $BUILD_SYS_PATH/shell/ini/davinci.ini -n $1"
		done
	exec_cmd "export ${keyword}=${old_sdk}"
else
	exec_cmd "upload.py -f $BUILD_SYS_PATH/shell/ini/davinci.ini -n $1"
fi

exit 0
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

