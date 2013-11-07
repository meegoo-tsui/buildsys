#!/bin/sh

reset
set -e
. $BUILD_SYS_PATH/shell/utils/base.sh
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -g "Enter your choice [yes - delete all code and repos !!!]:"
read choice
if [ "$choice" != "yes" ] ; then
	print-color.sh -r "Skip, nothing to do !"
	exit 1
fi

exec_cmd "sudo rm -rf /home/git/repositories/davinci"
exec_cmd "sudo rm -rf /home/git/repositories/st"
exec_cmd "sudo rm -rf /home/meegoo/workspace/davinci"
exec_cmd "sudo rm -rf /home/meegoo/workspace/st"
exec_cmd "sudo rm -rf /home/install/*"
exit 0
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
