#!/bin/sh

reset
#set -e
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
	print-color.sh -g "  --push for gitrepo-to-another-server"
	print-color.sh -g "  -u     for gitrepo-url"
	print-color.sh -g "  -n     for gitrepo-server-name"	
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
function do_push() 
{
	# http://vxtindia.com/blog/how-to-migrate-github-repo-to-another-server-including-all-branches-and-tags/
	if [ ! -d .git ]; then
		print-color.sh -r "Error: not a git repos !"
		exit 1
	fi
	if [ ! -f .git/config.bak ]; then
		exec_cmd "cp .git/config .git/config.bak"
	fi

	if [ $# != 2 ]; then
		print-color.sh -g "Usage:"
		print-color.sh -g "$0 git@192.168.1.10:qt.git server"
		exit 1
	fi
	server=$2

	for remote in `git config -l | grep ^remote.$server`; do
			print-color.sh -g $remote
		done
	if [ "$remote" == "" ]; then
		git remote add $server $1
	else
		return
	fi

	for push in `git config -l | grep ^remote.$server.push`; do
			print-color.sh -g $push
		done

	if [ "$push" == "" ]; then
		git config --add remote.$server.push '+refs/heads/*:refs/heads/*'
		git config --add remote.$server.push '+refs/tags/*:refs/tags/*'
	fi

	for branch in `git branch -a --no-merged | grep remotes | grep -v HEAD | grep -v master`; do
		for branch_new in `git branch -a --no-merged | grep -v remotes | grep -v HEAD | grep -v master | grep "${branch##*/}$"`; do
			print-color.sh -g "branch: $branch_new exist"
			done
		if [ "$branch_new" == "" ]; then
			print-color.sh -g "branch: $branch_new track"
			git branch --track ${branch##*/} $branch
		fi
	done
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ $# -eq 0 ];then
	print_help
fi
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
args=`getopt -o "bdcmsu:n:h" -l "help,push" -- "$@"`
eval set -- $args
for i;do
	case $i in
		-b)         action="backup";  shift 1;;
		-d)         action="diff";    shift 1;;
		-c)         action="config";  shift 1;;
		-m)         action="mark";    shift 1;;
		-s)         action="status";  shift 1;;
		--push)     action="push";    shift 1;;
		-u)         url="$2";         shift 2;;
		-n)         server="$2";      shift 2;;		
		-h|--help)  print_help;;
		--)                           shift;;
	esac
done
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ "$action" == "" ];then
	print_help
else
	do_${action} $url $server
fi 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

