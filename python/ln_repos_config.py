#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    ln_repos_config.py
#  @brief   生成git repos的config软链接文件。
#  @author  meegoo.tsui@gmail.com
#  @date    2013/9/12

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.cmd            import cmd

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## main function.
def main():
	printf.reset()

	path = "/home/git/repositories/"
	configs_list = os.popen("find " + path + " -name config").read().split("\n")
	for i in sorted(configs_list):
		if i != "":
			file_name = i.split(path)[1].replace(".git", "").replace("/", "-").replace("-config", ".config")
			command = "ln -sf " + i + " " + file_name
			cmd.do(command)

	sys.exit(0)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if __name__ == '__main__':
	main()
