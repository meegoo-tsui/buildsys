#!/bin/sh

TIMESTAMP=`date +%Y-%m-%d.%H-%M-%S`
GIT_PATH=/home/git/repositories/dm814x
REPOS_NAME=dm814x-dev.git
PWD_PATH=$PWD

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print-color.sh -g "Backup local git repos, wait ..."
if [ -d ${GIT_PATH}/${REPOS_NAME} ];then
	cd ${GIT_PATH}/${REPOS_NAME}/..
	cmd="sudo tar -jcf ${PWD_PATH}/${REPOS_NAME}.${TIMESTAMP}.tar.bz2 ${REPOS_NAME}"
	print-color.sh -g "$cmd"
	$cmd
	cmd="sudo chown ${USER}:${USER} ${PWD_PATH}/${REPOS_NAME}.${TIMESTAMP}.tar.bz2"
	print-color.sh -g "$cmd"
	$cmd
	cd -
else
	print-color.sh -r "Error path: ${GIT_PATH}/${REPOS_NAME}"
	exit 1
fi
exit 0

