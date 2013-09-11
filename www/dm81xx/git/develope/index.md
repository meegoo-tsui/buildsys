## <font color="green">dm81xx develop</font> ##

<p align="left">
[返回](/dm81xx/)
<p>
<hr />

*	<font color="blue">基本路径介绍</font>
<pre><code>
dm8148@dm8148-vm:dm814x-dev.git$ tree -L 2
.
├── bin
│   ├── dump-dm814x.sh                 <font color="blue">自动使用git克隆出对应的软件开发包</font>
│   ├── ini
│   ├── install-demo-dm814x.sh         <font color="blue">安装demo到根文件系统</font>
│   ├── install-project-dm814x.sh      <font color="blue">安装project到根文件系统</font>
│   ├── mkdev.py                       <font color="blue">生成设备节点到根文件系统</font>
│   ├── sdk-dm814x.sh                  <font color="blue">切换SDK软件包</font>
│   ├── src
│   ├── status-dm814x.sh               <font color="blue">软件包修改状态查看</font>
│   ├── upload-dm814x.sh               <font color="blue">更新所有修改到git服务器</font>
│   ├── yuv420sp.exe
│   └── yuy2.exe
├── demo
│   ├── board-support
│   ├── codec_engine
│   ├── linux-driver-examples
│   ├── omx
│   ├── syslink
│   ├── tvp5147                        <font color="blue">tvp5147补丁，测试工程</font>
│   └── tvp7002
├── doc                                <font color="blue">开发相关文档</font>
│   ├── dm8127
│   ├── dm8148
│   ├── nand
│   ├── tvp
│   └── www
├── project
│   ├── build.ini                      <font color="blue">编译配置文件，此处包含多个项目的编译</font>
│   ├── filesys                        <font color="blue">制作根文件系统</font>
│   ├── kernel
│   ├── rdk
│   ├── sdk
│   └── uboot
└── rules                              <font color="blue">Makefile 包含文件</font>
    ├── environment-setup
    ├── ezsdk_5_05_02_00
    ├── ipnc_rdk_ga_release3.5.0
    ├── Rules.make
    └── ti81xx-psp-04.04.00.02
</code></pre>

*	<font color="blue">声明</font>
<pre><code>
<font color="red">
基本开发框架，需要调整，可以任意修改。
</font>
</code></pre>

<hr />
<p align="right">
[返回](/dm81xx/)
<p>

