#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    config_dev_env.py
#  @brief   环境工具，修改$HOME/.bashrc，自动设置环境变量。
#  @author  meegoo.tsui@gmail.com
#  @date    2013/03/15

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys, commands

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# buildsys to system path
_buildsys = os.environ["BUILD_SYS_PATH"] + "/python"
if _buildsys not in sys.path:
	sys.path.insert(0, _buildsys)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from utils.printf   import printf
from utils.env      import env

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## .bashrc文件路径。
env_file = os.path.expandvars("$HOME/.bashrc")
## 修改标志字符串。
env_flag = "# Configure davinci dev ENV"
## 添加内容。
env_content = \
  "\n#" + ">"*79 + "\n" + env_flag + "\n" + \
  "export EXE_INSTALL="   + env.home + "/install\n" + \
  "export SERVER_IP=192.168.1.10 # git和svn托管服务器\n" + \
  "export TFTPBOOT=/tftpboot\n" + \
  "export NFSBOOT=$EXE_INSTALL/nfsboot\n" + \
  "export TARGET_MAC=" + ':'.join(str(x) for x in env.hostmac().split(":")[:-1]) + ":03\n" + \
  "export TARGET_IP="  + '.'.join(str(x) for x in env.hostip().split(".")[:-1])  + ".30\n" + \
  "export HOST_IP="    + env.hostip() + "\n" + \
  "export GATE_IP="    + '.'.join(str(x) for x in env.hostip().split(".")[:-1])  + ".1\n"  + \
  "export MASK_IP=255.255.255.0\n" + \
  "\n# ARM GCC\n" + \
  "export PATH=/opt/arm-2009q1-203/bin:$PATH\n" + \
  "\n# DM814x dev ENV\n" + \
  "export DM814X_DEV=$WORKSPACE/local/dm814x/dm814x-dev.git\n" + \
  "export PATH=$DM814X_DEV/bin:$PATH\n" + \
  "export DM814X_SDK=ezsdk_5_05_02_00\n" + \
  "export DM814X_TARGET_NAME=dm814x\n" + \
  "export DM814X_TARGET_PROMPT=TI8148_EVM#\n" + \
  "\n# DM365 dev ENV\n" + \
  "export DM365_DEV=" + env.home + "/workspace/local/dm365/dm365-dev.git\n" + \
  "export PATH=$DM365_DEV/bin:$PATH\n" + \
  "export DM365_SDK=dvsdk_4_02_00_06\n" + \
  "export DM365_TARGET_NAME=dm365\n" + \
  "export DM365_TARGET_PROMPT=TI365_EVM#\n" + \
  "#" + "<"*79 + "\n"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 主函数。
def main():
	printf.reset()
	env.modify(env_file, env_flag , env_content)
	sys.exit(0)
if __name__ == '__main__':
	main()
