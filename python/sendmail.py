#! /usr/bin/python

################################################################################
# sendmail.py
#   send mail via smtp.
# meegoo.tsui@gmail.com
################################################################################
# import system library
import os, sys

# import tools path to python system path
sys.path.append(os.environ['BUILD_SYS_PATH'] + "/python")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.send           import send
from   utils.time           import time

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 收件人邮箱地址, xxx@qq.com
to      = ""

## 发件人邮箱地址, xxx@163.com
me      = ""

## 发件人邮箱密码
pwd     = ""

## 发件人邮箱服务器名，smtp.163.com
smtp    = ""

## 发件人邮箱服务器端口，25
port    = 0

## 邮件主题
subject = ""

## 邮件内容
info    = ""

################################################################################
# Main Function
def main():
	# start send
	printf.reset()
	time.push(os.path.abspath(__file__))

	# send
	send.to      = to
	send.me      = me
	send.pwd     = pwd
	send.smtp    = smtp
	send.port    = port
	send.subject = subject
	send.info    = info
	send.send()

	# end send
	time.pop()
	printf.silence("send done.")

	sys.exit(0)
if __name__ == "__main__":
	main()
################################################################################

