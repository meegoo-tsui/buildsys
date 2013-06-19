#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    mkdev.py
#  @brief   filesys工具，创建设备节点。
#  @author  meegoo.tsui@gmail.com
#  @date    2013/06/19

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.cmd            import cmd

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## makefile actions.
class mkdev:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## mkdevDict 参数字典
		## ("0", "1", "2", "3")
		##  路径  命令 名称  参数
		self.mkdevDict = []

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## mkdev
	def mkdev(self):
		printf.status("make dev ...")
		for x in range(0, len(self.mkdevDict)):
			if not os.path.isdir(self.mkdevDict[x][0]):
				cmd.do("mkdir -p " + self.mkdevDict[x][0])
			command = self.mkdevDict[x][1] + self.mkdevDict[x][0] \
			+ "/" + self.mkdevDict[x][2] + self.mkdevDict[x][3]
			cmd.do(command)
		return

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## mkdev对象。
mkdev = mkdev()
