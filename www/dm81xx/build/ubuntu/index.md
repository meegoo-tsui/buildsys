## <font color="green">TI DM81xx - ubuntu</font> ##

<p align="left">
[返回](/dm81xx/)
<p>
<hr />

linux发行版本使用ubuntu 12.04，TI官方推荐使用ubuntu 10.04 和 ubuntu 12.04，考虑到软件
升级的原因，选择最新的LST版本12.04。

*	<font color="blue">安装ubuntu 12.04</font>

	*	制作ubuntu 12.04 U盘安装镜像
	*	主机选择从U盘启动，安装ubuntu，磁盘空间不小于60GB
	
*	<font color="blue">更新软件</font>

	*	切换软件源，可选择sohu
	*	更新

*	<font color="blue">配置服务器</font>

	*	nfs: http://meegoo-tsui.github.io/blog/2012/06/05/nfs-server-and-usage/
	*	tftp： http://meegoo-tsui.github.io/blog/2012/06/05/tftp-server-and-usage/

*	<font color="blue">安装软件</font>

	* git: 版本管理系统
	* uboot-mkimage： 制作镜像
	* flex： 编译
	* bision： 编译

*	<font color="blue">设置环境变量</font>

	* 使用git下载编译工具集    
	
		*	mkdir -p $HOME/workspace; cd $HOME/workspace
		*	git clone git@server-ip:buildsys.git buildsys.git
		
	* 使用工具配置编译工具环境变量，工具自动修改～/.bashrc
	
		*	cd $HOME/workspace/buildsys.git/env
		*	. .env
		*	config_buildsys_env.py
		*	重启终端，使环境变量生效，修改结果如下：
<pre><code>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Configure buildsys ENV
export WORKSPACE=$HOME/workspace
export BUILD_SYS_PATH=/home/meegoo/workspace/buildsys.git
if [ -f $BUILD_SYS_PATH/env/.env ] ; then
	current_path=$PWD
	cd $BUILD_SYS_PATH/env
	. .env
	cd "$current_path"
fi
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
</code></pre>

	* 使用工具配置dm81xx相关环境变量，工具自动修改～/.bashrc
	
		*	config_davinci_env.py
		*	重启终端，使环境变量生效，修改结果如下：
<pre><code>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Configure davinci dev
export EXE_INSTALL=/home/install/$USER
export SERVER_IP=127.0.0.1 # git和svn托管服务器
export TFTPBOOT=$EXE_INSTALL/tftpboot
export NFSBOOT=$EXE_INSTALL/nfsboot
export TARGET_MAC=44:37:e6:93:46:03
export TARGET_IP=192.168.55.100
export HOST_IP=192.168.55.11
export GATE_IP=192.168.55.1
export MASK_IP=255.255.255.0
# davinci dev
export DAVINCI_DEV_PATH=$WORKSPACE/davinci/davinci-dev.git
export PATH=$DAVINCI_DEV_PATH/bin:$PATH
export DAVINCI_SDK=ezsdk_5_05_02_00
if [ -f $DAVINCI_DEV_PATH/rules/environment-setup ]; then
	. $DAVINCI_DEV_PATH/rules/environment-setup
fi
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
</code></pre>

*	<font color="blue">下载项目工程</font>

	*	dump.sh -p davinci -a

<pre><code>
meegoo@mg:workspace$ tree -L 2
.
├── buildsys.git
│   ├── config
│   ├── env
│   ├── python
│   ├── README.md
│   ├── shell
│   └── www
└── davinci
    ├── davinci-dev.git
    ├── davinci-env.git
    ├── ezsdk_5_05_02_00
    └── ipnc_rdk_ga_release3.5.0

</code></pre>

至此，基本完成环境的配置。

<font color="red">
[注意]
如果使用虚拟机，以上步骤已在虚拟机中的ubuntu中完成，无需进行以上操作。
</font>

<hr />
<p align="right">
[返回](/dm81xx/)
<p>

