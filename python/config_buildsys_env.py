#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    config_buildsys_env.py
#  @brief   环境工具，修改$HOME/.bashrc，自动设置环境变量。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from utils.printf   import printf
from utils.env      import env

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## .bashrc文件路径。
env_file = os.path.expandvars("$HOME/.bashrc")
## 修改标志字符串。
env_flag = "# Configure buildsys ENV"
## 添加内容。
env_content = "\n#" + ">"*79 + "\n" + env_flag + "\n" + \
"export WORKSPACE=$HOME/workspace\n" + \
"export BUILD_SYS_PATH="  + os.path.expandvars("$BUILD_SYS_PATH") + \
'''
if [ -f $BUILD_SYS_PATH/env/.env ] ; then
	current_path=$PWD
	cd $BUILD_SYS_PATH/env
	. .env
	cd "$current_path"
fi
''' + \
"#" + "<"*79 + "\n"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 主函数。
def main():
	printf.reset()
	env.modify(env_file, env_flag, env_content)
	sys.exit(0)
if __name__ == '__main__':
	main()
