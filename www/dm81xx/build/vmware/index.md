## <font color="green">TI DM81xx - vmware</font> ##

<p align="left">
[返回](/dm81xx/)
<p>
<hr />

如果使用vmware, 全部软件已经安装完成，环境变量和编译工具也安装完成，但为了清楚安装的内容，参看
[ubuntu 12.04 安装](/dm81xx/build/ubuntu)。安装完mware后，导入虚拟机镜像即可。

*	虚拟机软件： \\\\192.168.0.239\\飞行项目组资料共享\\开发类资料\\dm81xx\\tools\\VMware-workstation-full-8.0.1-528992.7z
*	虚拟机镜像： \\\\192.168.0.239\\飞行项目组资料共享\\开发类资料\\dm81xx\\vmware\\ubuntu12.04-dm8148-vm-xxx.7z
*	用户名： dm8148 密码： dm8148
*	/opt内容
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
</code></pre>

*	/home/dm8148/workspace内容
<pre><code>
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
├── install
│   ├── nfsboot
│   └── ti814x-evm
└── ipnc_rdk_ga_release3.5.0
    ├── board-support.git
    ├── component-sources.git
    ├── example-applications.git
    └── filesystem.git
</code></pre>

*	打开终端，显示内容如下：
<pre><code>
-============= .env =============-
Set env for buildsys...
PATH =
/home/dm8148/workspace/buildsys.git/python:/home/dm8148/workspace/buildsys.git/shell:/usr/lib/lightdm/lightdm:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
environment setup for ipnc_rdk_ga_release3.5.0
</code></pre>

<hr />
<p align="right">
[返回](/dm81xx/)
<p>

