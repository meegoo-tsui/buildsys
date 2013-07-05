#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    arg.py
#  @brief   所有工具的参数解析及帮助信息。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import sys
import getopt

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf   import printf

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 参数解析、帮助信息。
class arg:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具build.py的帮助信息。
	def build_usage(self):
		printf.printf(3, "Usage:\n" + "build.py " + "[options]")
		printf.printf(3, '''
Options:
-h | --help  print help info
-f           ini file path(default: build.ini)
-c           make clean
-m           make
-i           make install
-x           make others target in Makefile
-l           list all projects for build
-o           only make the project: -o [1,2,3 ...]
default      make clean, make, make install
''')

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具build.py的解析参数。
	def build_args(self):
		printf.status("parse args ...")
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hf:cmix:lo:", ["help"])
		except getopt.GetoptError , err:
			printf.warn(str(err)) # will print something like "option -a not recognized"
			self.build_usage()
			sys.exit(1)

		## build参数字典
		build_args = {'-f':'', '-c':0, '-m':0, '-i':0, '-x':'', '-l':'', '-o':''} # 默认为非法参数
		for o, a in opts:
			if   o in ("-h", "--help"):
				self.build_usage()
				sys.exit(1)
			elif o == "-f":
				build_args[o] = a
			elif o == "-c":
				build_args[o] = 1
			elif o == "-m":
				build_args[o] = 1
			elif o == "-i":
				build_args[o] = 1
			elif o == "-x":
				build_args[o] = ' '.join(str(n) for n in sys.argv[2:])
			elif o == "-l":
				build_args[o] = "true"
			elif o == "-o":
				build_args[o] = a
			else:
				assert False, "unhandled option"
				self.build_usage()
				sys.exit(1)

		return build_args

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具patch.py的帮助信息。
	def patch_usage(self):
		printf.printf(3, "Usage:\n" + "patch.py " + "[options]")
		printf.printf(3, '''
Options:
-h | --help  print help info
-f           ini file path
-a           action:
             0 - do patch
             1 - undo patch
             2 - create patch
-u           patch for untrack files, default without it
-l           list all projects for patch
-o           only patch the project: -o [1,2,3 ...]
''')

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具patch.py的解析参数。
	def patch_args(self):
		printf.status("parse args ...")
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hf:a:ulo:", ["help"])
		except getopt.GetoptError , err:
			printf.warn(str(err)) # will print something like "option -a not recognized"
			self.patch_usage()
			sys.exit(1)

		## patch参数字典，ini路径、patch动作
		patch_args = {'-f':'', '-a':-1, '-u':0, '-l':'', '-o':''} # 默认为非法参数
		for o, a in opts:
			if   o in ("-h", "--help"):
				self.patch_usage()
				sys.exit(1)
			elif o == "-f":
				patch_args[o] = a
			elif o == "-a":
				patch_args[o] = int(a)
			elif o == "-u":
				patch_args[o] = 1 # 需要对非托管文件打补丁
			elif o == "-l":
				patch_args[o] = "true"
			elif o == "-o":
				patch_args[o] = a
			else:
				assert False, "unhandled option"
				self.patch_usage()
				sys.exit(1)

		# 判断参数
		if (patch_args['-a'] < 0 and patch_args['-l'] == "") or patch_args['-f'] == "":
			self.patch_usage()
			sys.exit(1)

		return patch_args

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具check.py的帮助信息。
	def check_usage(self):
		printf.printf(3, "Usage:\n" + "check.py " + "[options]")
		printf.printf(3, '''
Options:
-h | --help  help info
-f           file path - must
-l           list all repos
-o           only checkout the repos: -o [1,2,3 ...]
-u           update(default without it)
''')

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具check.py的解析参数。
	def check_args(self):
		printf.status("parse args ...")
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hf:lo:u", ["help"])
		except getopt.GetoptError , err:
			printf.warn(str(err)) # will print something like "option -a not recognized"
			self.check_usage()
			sys.exit(1)

		## check参数字典，ini路径
		check_args = {'-f':'', '-l':'' , '-o':'', '-u':'false'} # 默认为非法参数
		for o, a in opts:
			if   o in ("-h", "--help"):
				self.check_usage()
				sys.exit(1)
			elif o == "-f":
				check_args[o] = a
			elif o == "-l":
				check_args[o] = "true"
			elif o == "-o":
				check_args[o] = a
			elif o == "-u":
				check_args[o] = "true"
			else:
				assert False, "unhandled option"
				self.check_usage()
				sys.exit(1)

		# 判断参数
		if check_args['-f'] == "":
			self.check_usage()
			sys.exit(1)

		return check_args

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具upload.py的帮助信息。
	def upload_usage(self):
		printf.printf(3, "Usage:\n" + "upload.py " + "[options]")
		printf.printf(3, '''
Options:
-h | --help  help info
-f           file path - must
-l           list all repos
-n           repos name(default is server)
''')

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具upload.py的解析参数。
	def upload_args(self):
		printf.status("parse args ...")
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hf:ln:", ["help"])
		except getopt.GetoptError , err:
			printf.warn(str(err)) # will print something like "option -a not recognized"
			self.upload_usage()
			sys.exit(1)

		## upload参数字典，ini路径
		upload_args = {'-f':'', '-l':'' , '-n':'server'} # 默认为非法参数
		for o, a in opts:
			if   o in ("-h", "--help"):
				self.upload_usage()
				sys.exit(1)
			elif o == "-f":
				upload_args[o] = a
			elif o == "-l":
				upload_args[o] = "true"
			elif o == "-n":
				upload_args[o] = a
			else:
				assert False, "unhandled option"
				self.upload_usage()
				sys.exit(1)

		# 判断参数
		if upload_args['-f'] == "":
			self.upload_usage()
			sys.exit(1)

		return upload_args

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具svn.py或git.py的帮助信息。
	def repos_usage(self, repos):
		printf.printf(3, "Usage:\n" + repos + ".py " + "[options]")
		printf.printf(3, '''
Options:
-h | --help  print help info
-m           list modify files
-d           list delete files
-o           list others files
-b           backup all repost
-s           repos status
-r           revert repos
-p           Path name (folder)
''')

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具svn.py或git.py的解析参数。
	def repos_args(self, repos):
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hmdobsrp:", ["help"])
		except getopt.GetoptError , err:
			printf.warn(str(err)) # will print something like "option -a not recognized"
			self.repos_usage(repos)
			sys.exit(1)

		## svn.py或git.py
		repos_args = {'-m':'', '-d':'' , '-o':'', '-b':'', '-s':'', '-r':'', '-p':''} # 默认为非法参数
		for o, a in opts:
			if   o in ("-h", "--help"):
				self.repos_usage(repos)
				sys.exit(1)
			elif o == "-p":
				repos_args[o] = a
			else:
				repos_args[o] = "true"

		return repos_args

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具links.py的帮助信息。
	def links_usage(self):
		printf.printf(3, "Usage:\n" + "links.py " + "[options]")
		printf.printf(3, '''
Options:
-h | --help  print help info
-s           source folder
-d           link folder
''')

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具links.py的解析参数。
	def links_args(self):
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hs:d:", ["help"])
		except getopt.GetoptError , err:
			printf.warn(str(err)) # will print something like "option -a not recognized"
			self.links_usage()
			sys.exit(1)

		links_args = {'-s':'', '-d':''} # 默认为非法参数
		for o, a in opts:
			if   o in ("-h", "--help"):
				self.links_usage()
				sys.exit(1)
			else:
				links_args[o] = a
		return links_args

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## mk_chk_ini.py help info
	def mk_chk_ini_usage(self):
		printf.printf(3, "Usage:\n" + "mk_chk_ini.py " + "[options]")
		printf.printf(3, '''
Options:
-h | --help  print help info
-p           path for git repos(folder)
-f           output file
-m           clone at mirror(default normal clone)
''')

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## mk_chk_ini.py args
	def mk_chk_ini_args(self):
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hp:f:m", ["help"])
		except getopt.GetoptError , err:
			printf.warn(str(err)) # will print something like "option -a not recognized"
			self.mk_chk_ini_usage()
			sys.exit(1)

		mk_chk_ini_args = {'-p':'', '-f':'', '-m':''} # 默认为非法参数
		for o, a in opts:
			if   o in ("-h", "--help"):
				self.mk_chk_ini_usage()
				sys.exit(1)
			elif o == "-m":
				mk_chk_ini_args[o] = "true"
			else:
				mk_chk_ini_args[o] = a
		if mk_chk_ini_args['-p'] == "" or mk_chk_ini_args['-f'] == "":
			self.mk_chk_ini_usage()
			sys.exit(1)		
		return mk_chk_ini_args

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## git_add_remote.py help info
	def git_add_remote_usage(self):
		printf.printf(3, "Usage:\n" + "git_add_remote.py " + "[options]")
		printf.printf(3, '''
Options:
-h | --help  print help info
-u           new url
-p           print ini(use for gitosis.conf)
-n           server name(default is server)
example:
	git_add_remote.py -u git@192.168.1.10:github/ -n server
''')

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## git_add_remote.py args
	def git_add_remote_args(self):
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hu:pn:", ["help"])
		except getopt.GetoptError , err:
			printf.warn(str(err)) # will print something like "option -a not recognized"
			self.git_add_remote_usage()
			sys.exit(1)

		git_add_remote_args = {'-u':'', '-p':'', '-n':'server'} # 默认为非法参数
		for o, a in opts:
			if   o in ("-h", "--help"):
				self.git_add_remote_usage()
				sys.exit(1)
			elif o == "-u":
				git_add_remote_args[o] = a
			elif o == "-p":
				git_add_remote_args[o] = "true"
			elif o == "-n":
				git_add_remote_args[o] = a
		if git_add_remote_args['-u'] == "":
			self.git_add_remote_usage()
			sys.exit(1)		
		return git_add_remote_args
	
	#---------------------------------------------------------------------------
## arg对象。
arg = arg()
