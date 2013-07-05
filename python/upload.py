#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    upload.py
#  @brief   upload git repos。
#  @author  meegoo.tsui@gmail.com
#  @date    2013/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.time           import time
from   utils.arg            import arg
from   utils.upload_repos   import upload_repos

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## main function.
def main():

	# start upload
	printf.reset()
	time.push(os.path.abspath(__file__))

	# check out the project
	upload_repos.upload_args = arg.upload_args()
	ini = upload_repos.upload_args['-f']
	upload_repos.upload(ini)

	# end upload
	time.pop()
	printf.silence("upload done.")
	sys.exit(0)

if __name__ == '__main__':
	main()
