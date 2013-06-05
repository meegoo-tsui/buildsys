#!/bin/bash

# http://vxtindia.com/blog/how-to-migrate-github-repo-to-another-server-including-all-branches-and-tags/
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ ! -d .git ]; then
	print-color.sh -r "Error: not a git repos !"
	exit 1
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ ! -f .git/config.bak ]; then
	cp .git/config .git/config.bak
	print-color.sh -g "Backup the config."
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ $# != 1 ]; then
	print-color.sh -g "Usage:"
	print-color.sh -g "$0 192.168.1.10:qt.git"
	exit 1
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
for remote in `git config -l | grep ^remote.local`; do
	print-color.sh -g $remote
done
if [ "$remote" == "" ]; then
	git remote add local git@$1
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
for push in `git config -l | grep ^remote.local.push`; do
	print-color.sh -g $push
done
if [ "$push" == "" ]; then
	git config --add remote.local.push '+refs/heads/*:refs/heads/*'
	git config --add remote.local.push '+refs/tags/*:refs/tags/*'
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
for branch in `git branch -a --no-merged | grep remotes | grep -v HEAD | grep -v master`; do
	for branch_new in `git branch -a --no-merged | grep -v remotes | grep -v HEAD | grep -v master | grep "${branch##*/}$"`; do
		print-color.sh -g "branch: $branch_new esxist"
	done
	if [ "$branch_new" == "" ]; then
		print-color.sh -g "branch: $branch_new track"
		git branch --track ${branch##*/} $branch
	fi
done

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
git push local
exit 0

