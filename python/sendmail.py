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
sys.path.append(os.environ['PWD'])
import data

################################################################################
# Main Function
def main():
	# start send
	printf.reset()
	time.push(os.path.abspath(__file__))

	# send
	send.to      = data.to
	send.me      = data.me
	send.pwd     = data.pwd
	send.smtp    = data.smtp
	send.port    = data.port
	send.subject = data.subject
	send.info    = data.info
	send.send()

	# end send
	time.pop()
	printf.silence("send done.")

	sys.exit(0)
if __name__ == "__main__":
	main()
################################################################################

