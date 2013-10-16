#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    patch_repos.py
#  @brief   依据ini配置文件执行源码路径的相关补丁操作。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/09

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, glob
import codecs

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.glb            import glb
from   utils.cmd            import cmd
from   utils.path           import path
from   utils.build_ini      import build_ini
from   utils.time           import time

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 对应仓库命令
patch_cmd = {}

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 依据ini配置文件执行源码路径的相关补丁操作。
class patch_repos:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## 当前section的ini参数
		self.ini_args   = {}
		## patch 参数字典
		self.patch_args = {}
		## 源码路径
		self.in_path    = ""
		## 源码路径 - 此路径下的非托管文件全部生成补丁
		self.in_all_path= []
		## 补丁路径
		self.out_path   = ""
		## repos根目录
		self.top_path   = ""
		## 补丁动作 - 0: 打上补丁，1：去除补丁，2：生成补丁
		self.action     = 0
		## git补丁命令
		self.cmd_git    = {
						    "list_modify":  "git status . -s | grep '^ M' | awk '{print $2}'", # 此命令仅显示当前目录下情况
						    "list_untrack": "git status . -s -u | grep '^??' | awk '{print $2}'", # 此命令仅显示当前目录下情况
						    "diff":         "git diff",
						    "level":        "  -p1 <  "
						  }
		## svn补丁命令
		self.cmd_svn    = {
						    "list_modify":  "svn status | grep \"^M\" | awk \'{print $2}\'",
						    "list_untrack": "svn status | grep \"^?\" | awk \'{print $2}\'",
						    "diff":         "svn diff",
						    "level":        "  -p0 <  "
						  }

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 判断是否已经打上补丁
	def is_patched(self):
		## 补丁标志文件
		patch_flag_file = self.in_path + "/" + glb.patch_flag
		if os.path.exists(patch_flag_file):
			printf.status("可以去除补丁。")
			return 1
		else:
			printf.status("可以打上补丁。")
			return 0

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 创建补丁标志文件
	def create_flag(self, yes): # yes = 1: create, yes = 0: delete
		## 补丁标志文件
		patch_flag_file = self.in_path + "/" + glb.patch_flag
		if yes == 1:
			cmd.do("touch " + patch_flag_file)
		else:
			cmd.do("rm -f " + patch_flag_file)

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 0 - 打上补丁， 1 - 去除补丁
	def patch(self, _a):
		global patch_cmd
		patch_cnt = 0
		
		if _a == 0:
			printf.silence("执行对源码打上补丁 ...")
			if self.is_patched() == 1:
				printf.warn("warnning： 源码已打上补丁！")
				return
			end_flag = ""
		else:
			printf.silence("执行对源码去除补丁 ...")
			if self.is_patched() == 0:
				printf.warn("warnning： 源码已去除补丁！")
				return
			end_flag = " -R"

		# 补丁类表
		patch_list = []
		patch_list.extend(glob.glob(self.out_path + "/*" + glb.patch_filetype))
		# 处理所有补丁
		for i in patch_list:
			# git和svn产生的补丁路径不一样，区别对待
			if i.find("git-") != -1:
				level = self.cmd_git['level']
			else:
				level = patch_cmd['level']
			patch_cnt = patch_cnt + 1
			cmd.do("patch -d " + self.top_path + level + i + end_flag)

		# 完成操作退出
		printf.status("Total patch: " + str(patch_cnt))
		if patch_cnt == 0 and _a == 0:
			self.create_flag(0)
		else:
			self.create_flag(not _a)

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 生成补丁
	def patch_new(self):
		global patch_cmd
		printf.silence("源码生成补丁 ...")
		patch_cnt = 0

		# 生成单个补丁文件
		repos_diff = self.out_path + "/" + self.ini_args[glb.source_repos] + ".diff"
		fp = codecs.open(repos_diff, "w", "utf-8")
		fp.close()

		out_modify  = os.popen(patch_cmd['list_modify']).read()
		# 判断是否需要对非托管文件打补丁
		out_untrack = ""
		if self.patch_args['-u'] == 0:
			for i in self.in_all_path: # 指定非托管文件打补丁路径，".h"、".c"、".cpp"、".mk"
				path.push()
				path.change(i)
				path_paste = i.replace(self.in_path + "/","")
				out_untrack_all = os.popen(patch_cmd['list_untrack']).read()
				path.pop()
				for i in out_untrack_all.split("\n"):
					if i == "":
						continue
					if i.upper().find(".H") == -1: # 文件过滤
						if i.upper().find(".C") == -1:
							if i.upper().find(".CPP") == -1:
								if i.upper().find(".MK") == -1:
									continue
					out_untrack = out_untrack + path_paste + "/" + i + "\n"
		else:
			out_untrack = os.popen(patch_cmd['list_untrack']).read()

		# 生成修改文件补丁
		cmd.do("rm -f " + self.out_path + "/*" + glb.patch_filetype) # 清除老补丁
		cmd.do("rm -f " + self.out_path + "/*.diff") # 清除老补丁
		patch_list = out_modify.split("\n")
		printf.status("Modify files: " + str(len(patch_list) - 1))
		for i in patch_list:
			if i == "":
				continue
			patch_cnt = patch_cnt + 1
			name = self.out_path + "/" + self.ini_args[glb.source_repos] + "-" + i.replace("/","_") + glb.patch_filetype
			cmd.do(patch_cmd['diff'] + " " + i + " > " + name)
			cmd.do(patch_cmd['diff'] + " " + i + " >> " + repos_diff)

		# 生成未托管文件补丁
		patch_list = out_untrack.split("\n")
		printf.status("Untrack files: " + str(len(patch_list) - 1))
		for i in patch_list:
			if i == "" or i.find(glb.patch_flag) != -1:
				continue
			patch_cnt = patch_cnt + 1
			name = self.out_path + "/" + "git-" + i.replace("/","_") + glb.patch_filetype
			cmd.tryit("git diff /dev/null " + i + " > " + name)
			cmd.tryit("git diff /dev/null " + i + " >> " + repos_diff)

		# 备份新生成的补丁
		if os.path.isdir(self.out_path):
			patch_list_new = []
			new_patchs = self.out_path + "/*" + glb.patch_filetype
			new_diff = self.out_path + "/*.diff"
			patch_list_new.extend(glob.glob(new_patchs))
			if len(patch_list_new) > 0:
				patch_bak_path = self.out_path + "/" + time.timestamp()
				cmd.do("mkdir -p " + patch_bak_path)
				cmd.do("cp " + new_patchs + " " + patch_bak_path)
				cmd.do("cp " + new_diff + " " + patch_bak_path)

		# 完成操作退出
		printf.status("Total patch: " + str(patch_cnt))
		if patch_cnt != 0:
			self.create_flag(1)
		else:
			self.create_flag(0)

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 执行补丁动作
	def do_patch(self):
		global patch_cmd

		printf.status("patch ...")
		# olny list all repos name
		if self.patch_args.has_key("-l"):
			if self.patch_args['-l'] != "":
				printf.status("only for list !")
				return 

		# patch all projects
		n = 0
		for i in build_ini.list_of_dict:
			# 只为当前使用的section执行补丁动作
			n = n + 1
			if self.patch_args.has_key("-o") and self.patch_args['-o'] != "":
				if self.patch_args['-o'] != str(n):
					printf.status("no need patch!")
					continue

			# 保存当前section的ini参数
			self.ini_args = i
			printf.silence("patch project: " + i[glb.project_name])
			# 设置源码路径
			if not i.has_key(glb.source_path):
				printf.warn("warnning: No source path !")
				continue
			self.in_path = os.path.abspath(i[glb.source_path])
			# 设置源码路径 - 此路径下的非托管文件全部生成补丁
			del self.in_all_path[:] # 清除上次的值
			for key_search in i:
				if key_search.find(glb.source_all_path) != -1:
					value = i[key_search]
					self.in_all_path.append(os.path.abspath(value))

			# 设置补丁路径
			if not i.has_key(glb.patch_path):
				printf.warn("warnning: No patch path !")
				continue
			self.out_path = i[glb.patch_path]

			# 创建补丁路径
			if not os.path.isdir(self.out_path):
				cmd.do("mkdir -p " + self.out_path)
			
			# 切换路径
			path.push()
			path.change(self.in_path)

			# 读取repos类型
			if not i.has_key(glb.source_repos):
				printf.warn("warnning: No source repos !")
				continue
			# 设置仓库命令
			self.top_path = self.in_path # 默认为根路径
			if i[glb.source_repos] == "svn":
				patch_cmd = self.cmd_svn
			elif i[glb.source_repos] == "git":
				patch_cmd     = self.cmd_git
				self.top_path = os.popen("git rev-parse --show-toplevel").read().split("\n")[0]
			else:
				printf.error("repos type error - " + i[glb.source_repos])

			# 补丁动作
			self.action = self.patch_args['-a']
			printf.silence("Patch action - " + str(self.action))
			if self.action == 0:   # 0: 打上补丁
				self.patch(0)
			elif self.action == 1: # 1：去除补丁
				self.patch(1)
			elif self.action == 2: # 2：生成补丁
				self.patch_new()

			# 切回路径
			path.pop()

		return

## patch对象.
patch_repos = patch_repos()
