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
	
	if git_args['-p'] != "":
		path.push()
		path.change(git_args['-p'])

	if git_args['-m'] == "true":
		os.system("git status -s | grep '^ M' | awk '{print $2}'")
	elif git_args['-d'] == "true":
		os.system("git status -s | grep '^ D' | awk '{print $2}'")
	elif git_args['-o'] == "true":
		os.system("git status -s | grep '^??' | awk '{print $2}'")
	
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	
	elif git_args['-b'] == "true":
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
	elif git_args['-s'] == "true":
		#printf.reset()
		printf.status("repos status")
		current_path = os.getcwd()
		if(os.path.exists(".git")):
			printf.silence("\n" + "+"*80)
			printf.silence(current_path)
			cmd.do("git status")
		else:
			n = 1
			for root, dirs, files in os.walk(current_path):	
				if '.git' in dirs:
					del dirs[:]
					printf.silence("\n" + "+"*80)
					printf.silence(str(n) + " - " + root)
					n = n + 1
					path.change(root)
					info = os.popen("git status -s | grep '^ M' | awk '{print $2}'").read()
					if(info != ""):
						printf.silence("-m:")
						printf.printf(1, info)

					info = os.popen("git status -s | grep '^ D' | awk '{print $2}'").read()
					if(info != ""):
						printf.silence("-d:")
						printf.printf(1, info)

					info = os.popen("git status -s | grep '^??' | awk '{print $2}'").read()
					if(info != ""):
						printf.silence("-o:")
						printf.printf(1, info)
					cmd.do("git status")					
					path.change(current_path)

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	elif git_args['-r'] == "true":
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

	if git_args['-p'] != "":
		path.pop()
	sys.exit(0)

if __name__ == '__main__':
	main()
