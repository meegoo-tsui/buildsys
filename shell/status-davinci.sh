#/bin/sh

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
. $BUILD_SYS_PATH/shell/utils/base.sh
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
reset
exec_cmd "git.py -s -p $WORKSPACE/buildsys.git"
exec_cmd "git.py -s -p $DAVINCI_DEV_PATH"
exec_cmd "git.py -s -p $DAVINCI_ENV_PATH"
exec_cmd "git.py -s -p $DAVINCI_DEV_PATH/../$DAVINCI_SDK"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
exit 0

