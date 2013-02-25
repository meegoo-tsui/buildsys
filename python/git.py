#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    git.py
#  @brief   git工具，显示相关异常文件。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/10/06

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.arg            import arg
from   utils.path           import path
from   utils.cmd            import cmd

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def revert():
	if(not os.path.exists(".git")):
		printf.warn("Not a git repos !")
		return

	git_cmd = "git status -s | grep '^ M' | awk '{print $2}'"
	info = os.popen(git_cmd).read()
	if(info != ""):
		printf.silence("revert -m:")
		os.system(git_cmd + " | xargs git checkout")

	git_cmd = "git status -s | grep '^ D' | awk '{print $2}'"
	info = os.popen(git_cmd).read()
	if(info != ""):
		printf.silence("revert -d:")
		os.system(git_cmd + " | xargs git checkout")

	git_cmd = "git status -s | grep '^??' | awk '{print $2}'"
	info = os.popen(git_cmd).read()
	if(info != ""):
		printf.silence("revert -o:")
		os.system(git_cmd + " | xargs rm -rf")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## main function.
def main():

	git_args = arg.repos_args("git")
	if git_args == "-m":
		os.system("git status -s | grep '^ M' | awk '{print $2}'")
	elif git_args == "-d":
		os.system("git status -s | grep '^ D' | awk '{print $2}'")
	elif git_args == "-o":
		os.system("git status -s | grep '^??' | awk '{print $2}'")
	
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	
	elif git_args == "-b":
		printf.reset()
		printf.status("repos backup")
		current_path = os.getcwd()
		if(os.path.exists(".git")):
			printf.status("Top at git repos")
		else:
			n = 1
			for r in os.walk(current_path).next()[1]:
				printf.silence("\n" + "+"*80)
				printf.silence(str(n) + " - " + r)
				path.change(current_path + "/" + r)
				n = n + 1
				if(not os.path.exists(".git")):
					printf.warn("Not a git repos - " + r)
					path.change(current_path)
					continue
				rev = os.popen("git rev-parse HEAD").read().split("\n")[0]
				path.change(current_path)
				# tar the repos
				tar = r + "." + rev + ".tar.bz2"
				if(not os.path.isfile(tar)):
					cmd.do("tar -jcf " + tar + " " + r)

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	elif git_args == "-s":
		printf.reset()
		printf.status("repos status")
		current_path = os.getcwd()
		if(os.path.exists(".git")):
			printf.status("Remote URL:")
			os.system("git remote -v")
			printf.status("Remote Branches: ")
			os.system("git branch -r")
			if os.path.isfile(".git/config"):
				printf.status("== Configuration .git/config")
				os.system("cat .git/config")
				printf.status("== Most Recent Commit")
			os.system("git --no-pager log --max-count=1")
		else:
			n = 1
			for r in os.walk(current_path).next()[1]:
				printf.silence("\n" + "+"*80)
				printf.silence(str(n) + " - " + r)
				path.change(current_path + "/" + r)
				n = n + 1
				if(not os.path.exists(".git")):
					printf.warn("Not a git repos - " + r)
					path.change(current_path)
					continue

				info = os.popen("git status -s | grep '^ M' | awk '{print $2}'").read()
				if(info != ""):
					printf.silence("-m:")
					printf.printf(3, info)

				info = os.popen("git status -s | grep '^ D' | awk '{print $2}'").read()
				if(info != ""):
					printf.silence("-d:")
					printf.printf(3, info)

				info = os.popen("git status -s | grep '^??' | awk '{print $2}'").read()
				if(info != ""):
					printf.silence("-o:")
					printf.printf(3, info)

				path.change(current_path)		

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	elif git_args == "-r":
		printf.reset()
		printf.status("repos revert")
		current_path = os.getcwd()
		if(os.path.exists(".git")):
			revert()
		else:
			n = 1
			for r in os.walk(current_path).next()[1]:
				printf.silence("\n" + "+"*80)
				printf.silence(str(n) + " - " + r)
				path.change(current_path + "/" + r)
				revert()
				path.change(current_path)
				n = n + 1

	sys.exit(0)

if __name__ == '__main__':
	main()
