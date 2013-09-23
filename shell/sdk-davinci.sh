#!/bin/sh

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
sdk=(ipnc_rdk_ga_release3.5.0 dvr_rdk_ga_release4.0.0)
len=${#sdk[*]}
keyword=DAVINCI_SDK

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
current_sdk()
{
	find=`grep $keyword ~/.bashrc`
	if [ "$find" == "" ]; then
		print-color.sh -r "ERROR:"
		print-color.sh -r " Need config env: config_davinci_env.py"
		exit 1
	fi
	print-color.sh -g "Current SDK:"
	echo "$find"
}

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
get_choice()
{
	print-color.sh -g "Change davinci SDK:"
	for (( i=0; i<len; i++ ))
		do 
			echo "$i: ${sdk[$i]}"
		done
	print-color.sh -g "Enter your choice [x - exit]:"
	read choice
	if [ "$choice" == "" ] || [ "$choice" == "x" ] ; then
		print-color.sh -r "Skip, nothing to do !"
		exit 1
	fi
	new=${sdk[$choice]}
	if [ "$new" == "" ]; then
		print-color.sh -r "Error choice: $choice"
		exit 1
	fi
	sed -i 's/DAVINCI_SDK.*/DAVINCI_SDK='"$new"'/g' ~/.bashrc
}

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
warning()
{
	print-color.sh -r "Warning: need restart the terminal !"
}

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
current_sdk
get_choice
current_sdk
warning
exit 0

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

