#! /usr/bin/python

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# replace the env name with value
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# import system labrary
import os, sys

# import tools path to python system path
sys.path.append(os.environ['BUILD_SYS_PATH'] + "/python")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.cmd            import cmd

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
env_name_dict = [
"TARGET_IP",
"HOST_IP",
"GATE_IP",
"MASK_IP",
"PLATFORM",
"NFSBOOT",
"DAVINCI_TARGET_PROMPT"
]

################################################################################
# Main Function
def main():
	# Judge args
	printf.reset()
	if len(sys.argv) != 3:
		printf.silence("Usage:")
		printf.silence(sys.argv[0] + " [input file] [output file]")
		sys.exit(1)
	if not os.path.isfile(sys.argv[1]):
		printf.error("Not a file - " + sys.argv[1])

	# print env
	printf.status("All env ...")
	for x in range(0, len(env_name_dict)):
		printf.silence(env_name_dict[x] + " = " + os.environ[env_name_dict[x]])

	# copy and replace
	cmd.do("cp -f " + sys.argv[1] + " " + sys.argv[2])
	for x in range(0, len(env_name_dict)):
		replace = "sed -i \'s" + "|$(" + env_name_dict[x] + ")|" + os.environ[env_name_dict[x]] + "|g\' " + sys.argv[2]
		cmd.do(replace)

	sys.exit(0)
if __name__ == "__main__":
	main()
################################################################################

