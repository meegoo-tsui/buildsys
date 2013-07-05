#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    upload_repos.py
#  @brief   依据ini配置文件执行源码的upload。
#  @author  meegoo.tsui@gmail.com
#  @date    2013/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys
import ConfigParser

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.cmd            import cmd
from   utils.path           import path

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 依据ini配置文件执行源码的upload。
class upload_repos:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## upload 参数字典
		self.upload_args = {}

		## default input ini file.
		self.ini        = ""

		## parser for repos.ini
		self.configIni = ConfigParser.ConfigParser()

		## 字典{"name":["path", "action"]
		self.dict      = {}

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## upload
	def upload(self, ini):
		self.ini = ini
		printf.status("parse ini ...")
		if not os.path.exists(self.ini):
			printf.error(self.ini + " is not exsit !")
			sys.exit(1)

		# read ini
		fp = open(self.ini,"r")
		self.configIni.readfp(fp)
		fp.close()

		# parse all sections
		for opts in self.configIni.options("repos"):
			# name
			i = opts.split(".repos")[0]
			# path
			j = os.path.expandvars(self.configIni.get("path", i + ".path"))
			# repos
			k = self.configIni.get("repos", opts)
			self.dict[i] = [j, k]

		# print upload info
		cnt = 0
		printf.status("repos status ...")
		for i in sorted(self.dict):
			cnt = cnt + 1
			printf.silence(str(cnt) + " - " + i)
			repos_path = self.dict[i][0] + "/" + i
			printf.silence("path - " + repos_path)										
			if not os.path.isdir(repos_path):
				printf.error("Error path - " + repos_path + "\n")

		# olny list all repos name
		if self.upload_args['-l'] != "":
			return 0

		# upload
		cnt = 0
		printf.status("upload ...")
		for i in sorted(self.dict):
			cnt = cnt + 1
			printf.silence(str(cnt) + " - " + i)
			repos_path = self.dict[i][0] + "/" + i
			if os.path.isdir(repos_path):
				path.push()
				path.change(repos_path)
				if self.dict[i][1].find("git clone") != -1:
					printf.silence("git repos")
					cmd.do("git push " + self.upload_args['-n'])
				else:
					printf.warn("unkown - " + self.dict[i][1])
				path.pop()

## upload对象.
upload_repos = upload_repos()
