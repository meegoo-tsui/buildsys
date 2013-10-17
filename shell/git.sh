#!/bin/sh

reset
set -e
. $BUILD_SYS_PATH/shell/utils/base.sh
. $BUILD_SYS_PATH/shell/utils/sdk.sh
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function print_help() 
{ 
	print-color.sh -y "git.sh:"
	print-color.sh -g "  -b     for git backup patch"
	print-color.sh -g "  -d     for git Diff"
	print-color.sh -g "  -c     for git config env vars"
	print-color.sh -g "  -m     for git mark nop file in nop folder"
	print-color.sh -g "  -s     for git status"
	print-color.sh -g "  --sdk  for git mark nop file in nop folder"
	exit 1
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function do_backup() 
{ 
	exec_cmd "patch.py -f backup.ini -a 2 -u"
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function do_diff() 
{ 
	exec_cmd "git diff . | colordiff"
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function do_config() 
{
	# name and email
	exec_cmd "git config --global user.name \"meegoo tsui\""
	exec_cmd "git config --global user.email \"meegoo.tsui@gmail.com\""

	# chinese font
	exec_cmd "git config --global gui.encoding utf-8"
	exec_cmd "git config --global i18n.commitencoding utf-8"
	exec_cmd "git config --global i18n.logoutputencoding gbk"

	# fie mode and edit
	exec_cmd "git config --global core.fileMode false"
	exec_cmd "git config --global core.editor vim"

	# global ignore
	exec_cmd "git config --global core.excludesfile '~/.gitignore'"

	exec_cmd "echo \"# buildsys\"    > ~/.gitignore"
	exec_cmd "echo \"buildsys.mak\" >> ~/.gitignore"
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function do_mark() 
{
	find_cmd="find . -type d -empty"
	exec_cmd "$find_cmd"
	touch_cmd="$find_cmd -print0 | xargs -0 -I {} touch {}/.gitignore"
	exec_cmd "$touch_cmd"
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function do_status() 
{
	exec_cmd "git.py -s -p $WORKSPACE/buildsys.git"
	exec_cmd "git.py -s -p $DAVINCI_DEV_PATH"
	exec_cmd "git.py -s -p $DAVINCI_ENV_PATH"
	exec_cmd "git.py -s -p $DAVINCI_DEV_PATH/../$DAVINCI_SDK"
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
args=`getopt -o dcm -l help sdk -- "$@"`
eval set -- $args
for i;do
	case $i in
		-b) action="backup";shift 1;;
		-d) action="diff";shift 1;;
		-c) action="config";shift 1;;
		-m) action="mark";shift 1;;
		-s) action="status";shift 1;;
		--sdk) action="sdk";shift 1;;
		-h|--help)print_help;;
		--)shift;;
	esac
done
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ "$action" == "" ];then
	print_help
else
	do_${action}
fi 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

