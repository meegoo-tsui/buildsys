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
from   utils.cmd            import cmd

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
sys.path.append(os.environ['PWD'])
import data

################################################################################
# Main Function
def main():
	# start send
	printf.reset()
	
	time.push(os.path.abspath(__file__))

	# loop send mail
	current = 0
	scnt    = 0
	fcnt    = 0
	onetime = 16
	cmd.do("rm -f number.py*")
	cmd.do("random_number.py")
	fp = open("send_done", 'w')
	fp.close()
	import number
	maxcnt  = number.array_len/onetime
	while 1:
		if scnt > maxcnt:
			break
		pos0 = scnt * onetime
		pos1 = pos0 + onetime
		if pos1 > number.array_len:
			pos1 = number.array_len
		send.to      = number.name_array[pos0:pos1]
		send.me      = data.me[current]
		send.pwd     = data.pwd
		send.smtp    = data.smtp[current]
		send.port    = data.port[current]
		send.subject = data.subject
		send.info    = data.info
		printf.status(data.me[current])
		try:
			send.send()
			scnt = scnt + 1
			printf.status("sucess to send - " + str(scnt))
			printf.status("fail to send - " + str(fcnt))
			fp = open("send_done", 'a')
			fp.write(str(scnt) + " - " + str(send.to) + "\n")
			fp.close()
		except:
			fcnt = fcnt + 1
			current = current + 1  # change email user name
			if current >= len(data.me):
				current = 0 # again
			printf.warn("sucess to send - " + str(scnt))
			printf.warn("fail to send - " + str(fcnt))
			systime.sleep(3)

	# end send
	fp.close()
	time.pop()
	printf.silence("send done.")

	sys.exit(0)
if __name__ == "__main__":
	main()
################################################################################

