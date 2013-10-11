#/bin/sh

reset
print-color.sh -g "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print-color.sh -g "Install software as a ubuntu dev host ..."

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
exec_cmd()
{
	print-color.sh -g "$1"
	$1
}

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ $# != 0 ]; then
	exec_cmd "sudo apt-get update"
	exec_cmd "sudo apt-get upgrade"
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -y "install dev tools ..."
exec_cmd "sudo apt-get -y install u-boot-tools bison flex colordiff"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -y "config ..."
exec_cmd "sudo ln -sf /bin/bash /bin/sh"
exec_cmd "sudo chmod +s /bin/chmod"
exec_cmd "sudo chmod +s /bin/mknod"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -g "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print-color.sh -g "Install done."

