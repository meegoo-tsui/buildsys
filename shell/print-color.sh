#!/bin/bash
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ print-color.sh
#+   printf text with color
#+ author
#+   meegoo.tsui@gmail.com, 2012-06-28
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
. $BUILD_SYS_PATH/shell/utils/color.sh

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function print_help() 
{ 
	echo "${txtgrn}usage:${txtrst}"
	echo "${txtred}  print-color.sh -r "\"printf color - red\""   ${txtrst}"
	echo "${txtgrn}  print-color.sh -g "\"printf color - green\"" ${txtrst}"
	echo "${txtylw}  print-color.sh -y "\"printf color - yellow\""${txtrst}"
	echo "${txtblu}  print-color.sh -b "\"printf color - blue\""  ${txtrst}"
	echo "${txtpur}  print-color.sh -p "\"printf color - purple\""${txtrst}"
	echo "${txtcyn}  print-color.sh -c "\"printf color - cyan\""  ${txtrst}"
	echo "${txtwht}  print-color.sh -w "\"printf color - white\"" ${txtrst}"
	exit 1
}

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# global vars
color=$txtrst
comment=""

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# getopt
if [ $# -eq 0 ];then
	print_help
	exit 1
fi
args=`getopt -o r:g:y:b:p:c:w:h -l help -- "$@"`
eval set -- $args
for i;do
	case $i in
		-r) color=$txtred;comment=$2;shift 2;;
		-g) color=$txtgrn;comment=$2;shift 2;;
		-y) color=$txtylw;comment=$2;shift 2;;
		-b) color=$txtblu;comment=$2;shift 2;;
		-p) color=$txtpur;comment=$2;shift 2;;
		-c) color=$txtcyn;comment=$2;shift 2;;
		-w) color=$txtwht;comment=$2;shift 2;;	
		-h|--help)print_help;;
		--)shift;;
	esac
done

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
echo "${color}$comment${txtrst}"

