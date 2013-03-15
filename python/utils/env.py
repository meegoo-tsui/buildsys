#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    env.py
#  @brief   环境变量设置功能。
#  @author  meegoo.tsui@gmail.com
#  @date    2013/03/15

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys, commands

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf   import printf

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 环境变量设置功能。
class env:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		self.home = os.environ["HOME"]

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 得到主机IP
	def hostip(self):
		host_ip = ""
		ips_get = "/sbin/ifconfig | grep -i \"inet addr:\" | awk {'print $2'} | sed -ne 's/addr://p'"
		ips     = commands.getoutput(ips_get)
		ipsList = ips.split("\n")
		for i in ipsList:
			if i.startswith("127."):
				continue
			else:
				host_ip = i
		printf.status("Host IP - " + host_ip)
		return host_ip

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 得到主机MAC
	def hostmac(self):
		import uuid
		hostmac = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
		printf.status("Host MAC - " + hostmac)
		return hostmac

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 修改env文件，添加内容到文件尾
	def modify(self, filename, flag, content):
		# judge
		fp = open(filename, "r")
		for line in fp:
			if flag in line:
				fp.close()
				printf.status("With [" + flag + "] already.")
				sys.exit(0)
		fp.close()

		# modify
		fp = open(filename, "a")
		fp.write(content)
		fp.close()
		printf.status("Write [" + flag + "] success.")

		return

## env对象
env = env()
