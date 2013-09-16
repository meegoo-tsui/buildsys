#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    stdin.py
#  @brief   输出工具，空格转换为换行。
#  @author  meegoo.tsui@gmail.com
#  @date    2013/09/16

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## main function.
def main():

	data = sys.stdin.read().split(" ")
	for i in sorted(data):
		i = i.replace("\n", "")
		i = i.replace("\r", "")
		if i != "":
			print i

	sys.exit(0)

if __name__ == '__main__':
	main()
