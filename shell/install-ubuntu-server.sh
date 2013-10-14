#/bin/sh

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
. $BUILD_SYS_PATH/shell/utils/base.sh
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
reset
print-color.sh -g "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print-color.sh -g "Install software as a ubuntu server ..."
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ $# != 0 ]; then
	exec_cmd "sudo apt-get update"
	exec_cmd "sudo apt-get upgrade"
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -y "server: ssh"
exec_cmd "sudo apt-get -y install openssh-server"
exec_cmd "sudo /etc/init.d/ssh restart"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -y "server: samba"
exec_cmd "sudo apt-get -y install samba samba-common samba-common-bin system-config-samba"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -y "server: tftp"
exec_cmd "sudo apt-get -y install tftpd tftp xinetd"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -y "server: nfs"
exec_cmd "sudo apt-get -y install nfs-kernel-server"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -y "server: svn and git"
exec_cmd "sudo apt-get -y install apache2 subversion libapache2-svn python-subversion libapache2-mod-wsgi"
exec_cmd "sudo apt-get -y install openssh-server openssh-client git python-setuptools gitweb highlight"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -y "usefull tools"
exec_cmd "sudo apt-get -y install vim gnome-schedule"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -g "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print-color.sh -g "Install done."

