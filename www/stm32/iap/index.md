## <font color="green">ST STM32 - IAP</font> ##

<p align="left">
[返回](/stm32)
<p>
<hr />

*	终端工具： \\\\192.168.0.239\\飞行项目组资料共享\\开发类资料\\dm81xx\\tools\\SecureCRT7.0.rar

*	源码 - [http://192.168.0.239/gitweb/?p=repositories/stm32/stm32.git;a=summary](http://192.168.0.239/gitweb/?p=repositories/stm32/stm32.git;a=summary)

*	IAP, 程序大小限制在0x3000, 应用程序的起始位置为0x3000, 需重定位中断向量表

	*	引导程序 - stm32.git/demo/iap_uart
	
	*	应用程序 - stm32.git/demo/printf
	
	*	格式转换 - stm32.git/tool/hex2bin.exe
	
	*	传输模式 - Ymodem

<hr />
<p align="right">
[返回](/stm32)
<p>

