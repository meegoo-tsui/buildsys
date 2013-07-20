#! /usr/bin/python

################################################################################
# sendmail.py
#   send mail via smtp.
# meegoo.tsui@gmail.com
################################################################################
# import system library
import os, sys
import time as systime

# import tools path to python system path
sys.path.append(os.environ['BUILD_SYS_PATH'] + "/python")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.send           import send
from   utils.time           import time

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
sys.path.append(os.environ['PWD'])
import data
import number

################################################################################
# Main Function
def main():
	# start send
	printf.reset()
	time.push(os.path.abspath(__file__))

	# loop send mail
	scnt    = 0
	fcnt    = 0
	onetime = 16
	maxcnt  = number.array_len/onetime
	fp = open("send_done", 'w')
	fp.close()
	while 1:
		if scnt > maxcnt:
			break
		pos0 = scnt * onetime
		pos1 = pos0 + onetime
		if pos1 > number.array_len:
			pos1 = number.array_len
		send.to      = number.name_array[pos0:pos1]
		send.me      = data.me
		send.pwd     = data.pwd
		send.smtp    = data.smtp
		send.port    = data.port
		send.subject = data.subject
		send.info    = data.info
		try:
			send.send()
			scnt = scnt + 1
			printf.status("sucess to send - " + str(scnt))
			fp = open("send_done", 'a')
			fp.write(str(scnt) + " - " + str(send.to) + "\n")
			fp.close()
			systime.sleep(300)
		except:
			fcnt = fcnt + 1
			printf.warn("fail to send - " + str(fcnt))
			systime.sleep(600)

	# end send
	fp.close()
	time.pop()
	printf.silence("send done.")

	sys.exit(0)
if __name__ == "__main__":
	main()
################################################################################

