## <font color="green">git</font> ##

<p align="left">
[返回](/dm81xx/)
<p>
<hr />

Git 是当前最流行的版本控制程序之一，以下包含了 Git 的一些基本用法。

1.	<font color="blue">创建 git 仓库，初始化 git 仓库</font>

	*	mkdir project # 创建项目目录
	*	cd project # 进入到项目目录
	*	git init # 初始化 git 仓库。此命令会在当前目录新建一个 .git 目录，用于存储 git 仓库的相关信息

2.	<font color="blue">初始化提交</font>

	*	touch README
	*	git add . # 将当前目录添加到 git 仓库中， 使用 git add -A 则是添加所有改动的文档
	*	git commit -m "Initial commit"
	*	git remote add origin git@github.com:lugir/repo.git # 设置仓库

3.	<font color="blue">修补提交（修补最近一次的提交而不创建新的提交）</font>

	*	git commit --amend -m "commit message."
	
4.	<font color="blue">克隆仓库</font>

	*	git clone http://path/to/git.git # clone 的内容会放在当前目录下的新目录

5.	<font color="blue">将代码从本地回传到仓库</font>

	*	git push -u origin master

6.	<font color="blue">使用 git status 查看文件状态</font>

	*	git status

7.	<font color="blue">查看提交日志</font>

	*	git log # 查看提交信息
	*	git log --pretty=oneline # 以整洁的单行形式显示提交信息
	*	git log --stat # 查看提交信息及更新的文件

<hr />
<p align="right">
[返回](/dm81xx/)
<p>

