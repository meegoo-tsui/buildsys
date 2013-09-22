#/bin/sh

reset
print-color.sh -g "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print-color.sh -g "Install software as a ubuntu server ..."

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -g "update and upgrade ..."
sudo apt-get update
sudo apt-get upgrade

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -g "server: ssh"
sudo apt-get -y install openssh-server
sudo /etc/init.d/ssh restart

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -g "server: samba"
sudo apt-get -y install samba samba-common samba-common-bin system-config-samba

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -g "server: tftp"
sudo apt-get -y install tftpd tftp xinetd

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -g "server: nfs"
sudo apt-get -y install nfs-kernel-server

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -g "server: svn and git"
sudo apt-get -y install apache2 subversion libapache2-svn python-subversion
sudo apt-get -y install openssh-server openssh-client git python-setuptools

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -g "usefull tools"
sudo apt-get -y install vim

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -g "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print-color.sh -g "Install done."

