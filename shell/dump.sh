#!/bin/sh

reset
set -e
. $BUILD_SYS_PATH/shell/utils/base.sh
. $BUILD_SYS_PATH/shell/utils/sdk.sh
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function print_help() 
{ 
	print-color.sh -y "dump.sh:"
	print-color.sh -g "  -p  for project name - davinci, st ..."
	print-color.sh -g "  -a  for all"
	print-color.sh -g "  -m  for mirror"
	exit 1
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function do_dump()
{
	exec_cmd "check.py -f $BUILD_SYS_PATH/shell/ini/${1}.ini -u ${2}"
}

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ $# -eq 0 ];then
	print_help
fi
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
args=`getopt -o "p:amh" -l "help" -- "$@"`
eval set -- $args
for i;do
	case $i in
		-p)        project="$2"; shift 2;;
		-a)        all="all";    shift 1;;
		-m)        mirror="-m";  shift 1;;
		-h|--help) print_help;;
		--)                      shift;;
	esac
done
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ "$mirror" != "" ];then
	exec_cmd "export WORKSPACE=/media/MEEGOO/workspace"
fi
if [ "$project" == "davinci" ];then
	if [ "$all" != "" ]; then
		old_sdk=`echo ${!keyword}`
		for (( i=0; i<len; i++ ))
			do 
				exec_cmd "export ${keyword}=${sdk[$i]}"
				do_dump ${project} ${mirror}
			done
			exec_cmd "export ${keyword}=${old_sdk}"
	else
		do_dump ${project} ${mirror}
	fi
else
	do_dump ${project} ${mirror}
fi
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

