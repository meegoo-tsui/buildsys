#! /usr/bin/python
#coding=utf-8

# import system labrary
import os, sys, random

# import tools path to python system path
sys.path.append(os.environ['BUILD_SYS_PATH'] + "/python")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.time           import time

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
num_min    = 10000000
num_max    = 10000000000
same       = 0
active     = 0
total      = 100000
out        = "number.py"
name_array = []

################################################################################
# Main Function
def main():
	global num_min, num_max, same, active, total, out, name_arra

	printf.reset()
	time.push(os.path.abspath(__file__))

	printf.status("write file ...")
	fp = open(out, 'w')

	random.seed()
	for i in range(total):
		name = str(random.randrange(num_min, num_max))
		if name in name_array:
			same  = same + 1
			printf.status("same: " + name)
		else:
			active = active + 1
			name_array.append("\"" + str(name) + "@qq.com" + "\"")
	printf.status("same:   "  + str(same))
	printf.status("active: "  + str(active))
	printf.status("total:  " + str(total))
	printf.status("len(name_array): " + str(len(name_array)))

	fp.write("array_len  = " + str(active) + "\n")
	fp.write("name_array = [\n")
	for i in range(len(name_array)):
		fp.write(name_array[i] + ",")
		if((i+1)%16 == 0):
			fp.write("\n")
	fp.write("]\n")

	fp.close()
	time.pop()
	sys.exit(0)

if __name__ == "__main__":
	main()
################################################################################

