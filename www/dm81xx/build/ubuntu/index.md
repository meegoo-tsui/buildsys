## <font color="green">TI DM81xx - ubuntu</font> ##

<p align="left">
[返回](/dm81xx/)
<p>
<hr />

linux发行版本使用ubuntu 12.04，TI官方推荐使用ubuntu 10.04 和 ubuntu 12.04，考虑到软件
升级的原因，选择最新的LST版本12.04，10.04就不推荐使用了。
镜像放在服务器上，位置：系统镜像： \\\\192.168.0.239\\飞行项目组资料共享\\开发类资料\\dm81xx\\tools\\ubuntu-12.04-desktop-i386.iso。

*	<font color="blue">安装ubuntu 12.04</font>

	*	制作ubuntu 12.04 U盘安装镜像
	*	主机选择从U盘启动，安装ubuntu，磁盘空间不小于40GB
	
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
	* dm81xx工具集： 解压\\\\192.168.0.239\\飞行项目组资料共享\\开发类资料\\dm81xx\\tools\\dm81xx-toolset.tar.bz2到/opt，
	解压后路径：
<pre><code>
dm8148@dm8148-vm:opt$ tree -L 2
.
├── arm-2009q1-203
│   ├── arm-none-linux-gnueabi
│   ├── bin
│   ├── jre
│   ├── lib
│   ├── libexec
│   ├── README-arm-none-linux-gnueabi.html
│   ├── README-arm-none-linux-gnueabi.txt
│   ├── share
│   ├── uninstall
│   └── Uninstall_Sourcery_Gxx_Lite_for_ARM_GNU_Linux -> /opt/arm-2009q1-203-arm-none-linux-gnueabi/uninstall/Uninstall_Sourcery_Gxx_Lite_for_ARM_GNU_Linux/Uninstall_Sourcery_Gxx_Lite_for_ARM_GNU_Linux
├── dm814x_dev
│   ├── ezsdk_5_05_02_00
│   ├── ipnc_rdk_ga_release3.5.0
│   └── ti81xx-psp-04.04.00.02 -> ezsdk_5_05_02_00/
└── lost+found [error opening dir]
</code></pre>
	
*	<font color="blue">设置环境变量</font>

	* 使用git下载编译工具集    
	
		*	mkdir -p $HOME/workspace; cd $HOME/workspace
		*	git clone git@192.168.0.239:buildsys.git buildsys.git
		
	* 使用工具配置编译工具环境变量，工具自动修改～/.bashrc
	
		*	cd $HOME/workspace/buildsys.git/env
		*	. .env
		*	config_buildsys_env.py
		*	重启终端，使环境变量生效，修改结果如下：
<pre><code>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Configure buildsys ENV
export WORKSPACE=$HOME/workspace
export BUILD_SYS_PATH=/home/dm8148/workspace/buildsys.git
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
# Configure davinci dev ENV
export EXE_INSTALL=/home/dm8148/workspace/install
export SERVER_IP=192.168.0.239 # git and svn server
export TFTPBOOT=/tftpboot
export NFSBOOT=$EXE_INSTALL/nfsboot
export TARGET_MAC=00:0c:29:46:ae:03
export TARGET_IP=192.168.55.100
export HOST_IP=192.168.55.11
export GATE_IP=192.168.55.1
export MASK_IP=255.255.255.0
# ARM GCC
export PATH=/opt/arm-2009q1-203/bin:$PATH
# DM814x dev ENV
export DM814X_DEV=$WORKSPACE/dm814x-dev.git
export PATH=$DM814X_DEV/bin:$PATH
export DM814X_SDK=ipnc_rdk_ga_release3.5.0
export DM814X_TARGET_NAME=dm814x
export DM814X_TARGET_PROMPT=TI8148_EVM#
if [ -f $DM814X_DEV/rules/environment-setup ]; then
	. $DM814X_DEV/rules/environment-setup
fi
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
</code></pre>

*	<font color="blue">下载$WORKSPACE/dm814x-dev.git, 项目工程</font>

	*	cd $WORKSPACE
	*	git clone git@192.168.0.239:dm814x/dm814x-dev.git dm814x-dev.git
	*	重启终端
<pre><code>
dm8148@dm8148-vm:workspace$ tree -L 2
.
├── buildsys.git
│   ├── env
│   ├── python
│   ├── README.md
│   └── shell
└── dm814x-dev.git
    ├── bin
    ├── demo
    ├── doc
    ├── project
    └── rules
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

