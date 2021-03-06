#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    build.py
#  @brief   编译工具，使用当前路径下的build.ini作为配置文件。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys
from   datetime import datetime

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.glb            import glb
from   utils.time           import time
from   utils.arg            import arg
from   utils.build_ini      import build_ini
from   utils.make           import make

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## main function.
def main():
	# start build
	printf.reset()
	time.push(os.path.abspath(__file__))

	# build the project
	make.build_args  = arg.build_args()
	if make.build_args['-f'] == '':
		ini = os.getcwd() + "/" + glb.build_ini
	else:
		ini = make.build_args['-f']
	build_ini.parse(ini)
	make.do_makes()

	# end build
	time.pop()
	printf.silence("[" + str(datetime.now()) + "]: build done.")
	sys.exit(0)

if __name__ == '__main__':
	main()
