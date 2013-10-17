#/bin/sh

reset
set -e
. $BUILD_SYS_PATH/shell/utils/base.sh
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function print_help() 
{ 
	print-color.sh -y "install.sh:"
	print-color.sh -g "  -d        for install demo to filesys"
	print-color.sh -g "  -p        for install project to filesys"
	print-color.sh -g "  --server  for install software as ubuntu server"
	print-color.sh -g "  --dev     for install software as ubunut developer"
	exit 1
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function install_server()
{
	exec_cmd "sudo apt-get update"
	exec_cmd "sudo apt-get upgrade"

	print-color.sh -y "server: ssh"
	exec_cmd "sudo apt-get -y install openssh-server"
	exec_cmd "sudo /etc/init.d/ssh restart"

	print-color.sh -y "server: samba"
	exec_cmd "sudo apt-get -y install samba samba-common samba-common-bin system-config-samba"

	print-color.sh -y "server: tftp"
	exec_cmd "sudo apt-get -y install tftpd tftp xinetd"

	print-color.sh -y "server: nfs"
	exec_cmd "sudo apt-get -y install nfs-kernel-server"

	print-color.sh -y "server: svn and git"
	exec_cmd "sudo apt-get -y install apache2 subversion libapache2-svn python-subversion libapache2-mod-wsgi"
	exec_cmd "sudo apt-get -y install openssh-server openssh-client git python-setuptools gitweb highlight"

	print-color.sh -y "usefull tools"
	exec_cmd "sudo apt-get -y install vim gnome-schedule"
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function install_dev()
{
	exec_cmd "sudo apt-get update"
	exec_cmd "sudo apt-get upgrade"

	print-color.sh -y "install dev tools ..."
	exec_cmd "sudo apt-get -y install u-boot-tools bison flex colordiff"

	print-color.sh -y "config ..."
	exec_cmd "sudo ln -sf /bin/bash /bin/sh"
	exec_cmd "sudo chmod +s /bin/chmod"
	exec_cmd "sudo chmod +s /bin/mknod"
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ $# -eq 0 ];then
	print_help
fi
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
args=`getopt -o dp -l help server dev -- "$@"`
eval set -- $args
for i;do
	case $i in
		-d) action="demo";shift 1;;
		-p) action="project";shift 1;;
		--server) action="server";shift 1;;
		--dev) action="dev";shift 1;;
		-h|--help)print_help;;
		--)shift;;
	esac
done
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ "$action" == "" ];then
	print_help
else
	install_${action}
fi 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

