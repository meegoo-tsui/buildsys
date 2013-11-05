## <font color="green">TI DM81xx - build</font> ##

<p align="left">
[返回](/dm81xx/)
<p>
<hr />

不管使用何种开发包，编译的步骤都是一致的，只需运行命令切换开发包。编译的过程一般是三步，make clean，
make，make install，使用build.py进行了封装，使得有更大的灵活性，同时也支持自动补丁功能。

1.	<font color="blue">更行代码，前提条件是能访问服务器</font>
	*	在终端任何路径执行命令： `dump.sh -p davinci -a`
	*	更新后的工作路径如下：
<pre><code>
meegoo@mg:workspace$ tree -L 2
.
├── admin-gitolite
│   ├── gitolite-admin.git
│   └── gitolite.git
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

2.	<font color="blue">全部编译</font>
	*	编译路径
<pre><code>
meegoo@mg:base$ pwd
/home/meegoo/workspace/davinci/davinci-dev.git/project/base
</code></pre>
	*	编译配置文件内容如下：
<pre><code>
meegoo@mg:base$ cat build.ini 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ build.ini:
#+   project - configure file for build.py
#+ author:
#+   meegoo.tsui@gmail.com
#+ date:
#+   2013/02/04
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
[1_uboot_nand]
project.path  = $DAVINCI_DEV_PATH/project/base/uboot/nand
[2_kernel]
project.path  = $DAVINCI_DEV_PATH/project/base/kernel
[3_sdk]
project.path  = $DAVINCI_DEV_PATH/project/base/sdk
[4_filesys]
project.path  = $DAVINCI_DEV_PATH/project/base/filesys
</code></pre>
	*	编译动作
<pre><code>
meegoo@mg:base$ build.py
</code></pre>

3.	<font color="blue">编译结果</font>
	*	tftp: /home/install/meegoo/tftpboot
	*	nfs: /home/install/meegoo/nfsboot

4.	<font color="blue">切换软件开发包</font>
<pre><code>
meegoo@mg:base$ go.sh --sdk
Current SDK:
export DAVINCI_SDK=ezsdk_5_05_02_00
Change davinci SDK:
0: ipnc_rdk_ga_release3.5.0
1: ezsdk_5_05_02_00
Enter your choice [x - exit]:
</code></pre>
	重启终端后，重复1、2步即可。

5.	<font color="blue">项目编译之三步</font>

	进入项目路径， 如： cd $DAVICI_DEV/project/base/kernel
	1.	清除： build.py -c
	2.	编译： build.py -m
	3.	清除： build.py -i

	<font color="red">
	[注意]
	快速编译执行2、3步即可。
	</font>

<hr />
<p align="right">
[返回](/dm81xx/)
<p>

