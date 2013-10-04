## <font color="green">TI DM81xx - build</font> ##

<p align="left">
[返回](/dm81xx/)
<p>
<hr />

不管使用何种开发包，编译的步骤都是一致的，只需运行命令切换开发包。编译的过程一般是三步，make clean，
make，make install，使用build.py进行了封装，使得有更大的灵活性，同时也支持自动补丁功能。

1.	<font color="blue">更行代码，前提条件是能访问服务器192.168.0.239</font>
	*	在终端任何路径执行命令： `dump-dm814x.sh`
	*	更新后的工作路径如下：
<pre><code>
dm8148@dm8148-vm:workspace$ pwd
/home/dm8148/workspace
dm8148@dm8148-vm:workspace$ tree -L 2
.
├── buildsys.git
│   ├── env
│   ├── python
│   ├── README.md
│   └── shell
├── dm814x-dev.git
│   ├── bin
│   ├── demo
│   ├── doc
│   ├── project
│   └── rules
└── ezsdk_5_05_02_00
    ├── board-support.git
    ├── component-sources.git
    ├── example-applications.git
    └── filesystem.git
</code></pre>

2.	<font color="blue">全部编译</font>
	*	编译路径
<pre><code>
dm8148@dm8148-vm:base$ pwd
/home/dm8148/workspace/dm814x-dev.git/project/base
</code></pre>
	*	编译配置文件内容如下：
<pre><code>
dm8148@dm8148-vm:base$ cat build.ini 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ build.ini:
#+   project - configure file for build.py
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
[1_kernel]
project.path  = $DM814X_DEV/project/base/kernel
source.path   = $DM814X_DEV/../$DM814X_SDK/$KERNEL_BUILD_PATH
[2_sdk]
project.path  = $DM814X_DEV/project/base/sdk
source.path   = $DM814X_DEV/../$DM814X_SDK
[3_filesys]
project.path  = $DM814X_DEV/project/base/filesys
source.path   = $DM814X_DEV/../$DM814X_SDK/$FILESYS_BUILD_PATH
</code></pre>
	*	编译动作
<pre><code>
dm8148@dm8148-vm:base$ pwd
/home/dm8148/workspace/dm814x-dev.git/project/base
dm8148@dm8148-vm:base$ build.py
</code></pre>
	显示如下信息，表明编译成功：
<pre><code>
status
        change path: /home/dm8148/workspace/dm814x-dev.git/project/base
status
        /home/dm8148/workspace/buildsys.git/python/build.py - 0h:24m:33s
        build done.
</code></pre>

3.	<font color="blue">编译结果</font>
	*	tftp: /tftpboot
	*	nfs: ~/install/nfsboot/filesys-???

4.	<font color="blue">切换软件开发包</font>
<pre><code>
dm8148@dm8148-vm:base$ sdk-dm814x.sh 
Current SDK:
export DM814X_SDK=ezsdk_5_05_02_00
Change dm814x SDK:
0: ezsdk_5_05_02_00
1: ipnc_rdk_ga_release3.5.0
2: ti81xx-psp-04.04.00.02
Enter your choice [x - exit]:
1
</code></pre>
	重启终端后，重复1、2步即可。

5.	<font color="blue">项目编译之三步</font>

	进入项目路径， 如： cd $DM814X_DEV/project/base/kernel
	1.	清除： build.py -c
	2.	编译： build.py -m
	3.	清除： build.py -i

	<font color="red">
	[注意]
	快速编译执行2、3步即可。
	</font>

6.	<font color="blue">应用编译，以$DM814X_DEV/demo/tvp5147</font>
	1.	cd $DM814X_DEV/demo/tvp5147
	2.	打上补丁： ./patch
	3.	编译： ./go
	4.	保存修改后的补丁： ./save
	5.	工作完成，清除补丁： ./clear

	<font color="red">
	[注意]
	执行5步的时候必须执行第四步，看以前脚本的内容了解具体动作。
	</font>

<hr />
<p align="right">
[返回](/dm81xx/)
<p>

