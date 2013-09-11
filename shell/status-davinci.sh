#/bin/sh

reset
paths=("$NFSBOOT" "$TFTPBOOT" "$EXE_INSTALL")
len=${#paths[*]}
comment="++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

print-color.sh -g $comment
print-color.sh -g "repos - status"
git.py -s -p $DAVINCI_DEV_PATH/..

for (( i=0; i<len; i++ ))
	do
		if [ "${paths[$i]}" != "" ] && [ -d ${paths[$i]} ]; then
			print-color.sh -g $comment
			print-color.sh -g "${paths[$i]}"
			ls ${paths[$i]} -l
			echo
		fi
	done
exit

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
exit 0

