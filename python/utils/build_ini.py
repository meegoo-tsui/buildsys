#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    build_ini.py
#  @brief   解析build.ini配置文件。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys
import ConfigParser

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf   import printf
from   utils.glb      import glb

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 解析各种ini配置文件。
class build_ini:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## default input ini file.
		self.ini       = ""

		## parser for build.ini
		self.configIni = ConfigParser.ConfigParser()

		## 字典列表，每个section对应一个字典
		self.list_of_dict    = []

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 递归： 多次扩展，无source.path在build.ini就扩展
	def ini_expand(self, ini):
		printf.status("expand ini to " + ini)
		my_configIni = ConfigParser.ConfigParser()
		fp = open(ini,"r")
		my_configIni.readfp(fp)
		fp.close()
		for i in sorted(my_configIni.sections()):
			build_ini_file = os.path.expandvars(my_configIni.get(i, glb.project_path) + "/" + glb.build_ini)
			if my_configIni.has_option(i, glb.source_path):
				## 初始化字典	
				dictionary = {}
				dictionary[glb.project_name] = i

				## 读取所有option到字典
				for j in my_configIni.options(i):
					dictionary[j] = os.path.expandvars(my_configIni.get(i, j))
				self.list_of_dict.append(dictionary)
			else: # 无source.path扩展
				self.ini_expand(build_ini_file)

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## parser of ini file
	def parse(self, ini):
		# judge ini exists
		printf.status("parse ini ...")
		self.ini = ini
		if not os.path.exists(self.ini):
			printf.error(self.ini + " is not exsit !")
			sys.exit(1)

		# parse ini
		fp = open(self.ini,"r")
		self.configIni.readfp(fp)
		fp.close()

		# parse all sections
		self.ini_expand(self.ini)

		## 打印解析到的数据
		n = 0
		for i in self.list_of_dict:
			n = n + 1
			printf.silence("\nsection - " + str(n) + ":")
			for key in i.keys():
				printf.silence(key + " = " + i[key])

		return

## object of class ini.
build_ini = build_ini()
