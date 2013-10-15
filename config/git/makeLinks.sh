#/bin/sh

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
. $BUILD_SYS_PATH/shell/utils/base.sh
. $BUILD_SYS_PATH/shell/utils/sdk.sh
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
exec_cmd "ln -sf ../../.git/config buildsys.config"
exec_cmd "ln -sf ../../../../davinci/davinci-dev.git/.git/config davinci/davinci-dev.config"
exec_cmd "ln -sf ../../../../davinci/davinci-env.git/.git/config davinci/davinci-env.config"
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# davinci
for (( i=0; i<len; i++ ))
	do
		exec_cmd "ln -sf ../../../../../davinci/${sdk[$i]}/board-support.git/.git/config davinci/${sdk[$i]}/board-support.config"
		exec_cmd "ln -sf ../../../../../davinci/${sdk[$i]}/component-sources.git/.git/config davinci/${sdk[$i]}/component-sources.config"
		exec_cmd "ln -sf ../../../../../davinci/${sdk[$i]}/example-applications.git/.git/config davinci/${sdk[$i]}/example-applications.config"
		exec_cmd "ln -sf ../../../../../davinci/${sdk[$i]}/filesystem.git/.git/config davinci/${sdk[$i]}/filesystem.config"
	done
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# st
exec_cmd "ln -sf ../../../../st/stm32.git/.git/config st/stm32.config"
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

