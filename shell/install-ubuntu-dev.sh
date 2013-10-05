#/bin/sh

reset
print-color.sh -g "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print-color.sh -g "Install software as a ubuntu dev host ..."

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -g "update and upgrade ..."
sudo apt-get update
sudo apt-get upgrade

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -g "install dev tools ..."
sudo apt-get -y install u-boot-tools bison flex colordiff

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -g "config ..."
sudo ln -sf /bin/bash /bin/sh
sudo chmod +s /bin/chmod
sudo chmod +s /bin/mknod

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -g "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print-color.sh -g "Install done."

