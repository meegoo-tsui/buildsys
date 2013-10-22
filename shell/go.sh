#!/bin/sh

reset
set -e
. $BUILD_SYS_PATH/shell/utils/base.sh
. $BUILD_SYS_PATH/shell/utils/sdk.sh
ini="build.ini"
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function print_help() 
{ 
	print-color.sh -y "go.sh:"
	print-color.sh -g "  -p     for patch On"
	print-color.sh -g "  -c     for patch Clean"
	print-color.sh -g "  -s     for patch Save"
	print-color.sh -g "  -b     for project Build"
	print-color.sh -g "  -o     for project Only n"
	print-color.sh -g "  --sdk  for change the sdk"
	exit 1
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function do_on()
{
	if [ $# != 1 ]; then
		exec_cmd "patch.py -f $ini -a 0"	
	else
		exec_cmd "patch.py -f $ini -a 0 -o $1"
	fi
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function do_save()
{
	if [ $# != 1 ]; then
		exec_cmd "patch.py -f $ini -a 2"
	else
		exec_cmd "patch.py -f $ini -a 2 -o $1"
	fi
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function do_clean()
{
	if [ $# != 1 ]; then
		exec_cmd "patch.py -f $ini -a 1"	
	else
		exec_cmd "patch.py -f $ini -a 1 -o $1"
	fi
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function do_build()
{
	export FASTBUILD="1"
	if [ $# != 1 ]; then
		exec_cmd "build.py -f $ini -m -i"
	else
		exec_cmd "build.py -f $ini -m -i -o $1"
	fi
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function do_sdk() 
{
	current_sdk
	get_choice
	current_sdk
	warning
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ $# -eq 0 ];then
	print_help
fi
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
args=`getopt -o "pcsblo:hf:" -l "help,sdk" -- "$@"`
eval set -- $args
for i;do
	case $i in
		-p)        action="on";    shift 1;;
		-c)        action="clean"; shift 1;;
		-s)        action="save";  shift 1;;
		-b)        action="build"; shift 1;;
		-f)        ini="$2";       shift 2;;
		--sdk)     action="sdk";   shift 1;;
		-o)        only="$2";      shift 2;;
		-h|--help) print_help;;
		--)                        shift;;
	esac
done
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ "$action" == "" ];then
	print_help
else
	if [ "$only" == "" ];then
		do_${action}
	else
		do_${action} $only
	fi
fi 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

