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
env_flag = "# Configure davinci dev"
## 添加内容。
env_content = \
  "\n#" + ">"*79 + "\n" + env_flag + "\n" + \
  "export EXE_INSTALL=/home/install/$USER\n" + \
  "export SERVER_IP=127.0.0.1 # git和svn托管服务器\n" + \
  "export TFTPBOOT=$EXE_INSTALL/tftpboot\n" + \
  "export NFSBOOT=$EXE_INSTALL/nfsboot\n" + \
  "export TARGET_MAC=" + ':'.join(str(x) for x in env.hostmac().split(":")[:-1]) + ":03\n" + \
  "export TARGET_IP="  + '.'.join(str(x) for x in env.hostip().split(".")[:-1])  + ".100\n" + \
  "export HOST_IP="    + env.hostip() + "\n" + \
  "export GATE_IP="    + '.'.join(str(x) for x in env.hostip().split(".")[:-1])  + ".1\n"  + \
  "export MASK_IP=255.255.255.0\n" + \
  "\n# davinci dev\n" + \
  "export DAVINCI_DEV_PATH=$WORKSPACE/davinci/davinci-dev.git\n" + \
  "export PATH=$DAVINCI_DEV_PATH/bin:$PATH\n" + \
  "export DAVINCI_SDK=ipnc_rdk_ga_release3.5.0\n" + \
  "if [ -f $DAVINCI_DEV_PATH/rules/environment-setup ]; then\n" + \
  "	. $DAVINCI_DEV_PATH/rules/environment-setup\n" + \
  "fi\n" + \
  "#" + "<"*79 + "\n"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 主函数。
def main():
	printf.reset()
	env.modify(env_file, env_flag , env_content)
	sys.exit(0)
if __name__ == '__main__':
	main()
