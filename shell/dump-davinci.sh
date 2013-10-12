#!/bin/sh

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
. $BUILD_SYS_PATH/shell/utils/sdk.sh

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
exec_cmd()
{
	print-color.sh -g "$1"
	$1
}

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ $# != 0 ] && [ $1 == "all" ]; then
	old_sdk=`echo ${!keyword}`
	for (( i=0; i<len; i++ ))
		do 
			exec_cmd "export ${keyword}=${sdk[$i]}"
			exec_cmd "check.py -f $BUILD_SYS_PATH/shell/ini/davinci.ini -u"
		done
	exec_cmd "export ${keyword}=${old_sdk}"
else
	exec_cmd "check.py -f $BUILD_SYS_PATH/shell/ini/davinci.ini -u"
fi

exit 0
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

