python 环境移植
注意：以下文本所有"【】"都是标识符，需要去掉
本地代码位置：【C:\Users\linzg_64\Desktop\工作区\python离线发布】

python3.7.1为例
1.下载对应版本安装包【A】：https://www.python.org/ftp/python/3.7.1/python-3.7.1-amd64.exe， 放到 python离线发布 目录下
2.创建本地虚拟环境 【win_env_1】: 
	pip install virtualenv
	virtualenv win_env_1
3.进入并启动虚拟环境：
	cd C:\Users\linzg_64\win_env_1
	activate 进入 （deactivate 退出）
4.尝试运行项目代码（本地代码位置：C:\Users\linzg_64\Desktop\工作区\python离线发布\code\taiji\utilsTest\utils\taiji_count_tool.py）
	cd C:\Users\linzg_64\Desktop\工作区\python离线发布\code\taiji\utilsTest\utils\
	python taiji_count_tool.py
	(此时会报错，报错内容为缺少包，缺什么就下载什么)
5.下载所缺的包(下载xlwt为例)：
	pip install xlwt
6.运行通过后导出包列表信息(本地指定目录【D】：C:\Users\linzg_64\Desktop\工作区\python离线发布\packages)：
	cd C:\Users\linzg_64\Desktop\工作区\python离线发布
	md packages
	cd packages
	pip freeze > packages.txt
7.将包下载到指定目录:
	pip download -d . -r packages.txt
8.将 python离线发布 文件夹打包成一个zip包，放到新电脑中

9.切换到新主机(zip包解压到C:\Users\linzg_test_evn\Desktop\python离线发布)
10.安装python3
11.创建虚拟环境(本地路径：C:\lin，此时创建的虚拟环境名：lin)
	cd C:\
	md lin
	cd lin
	找到python安装目录 C:\Users\linzg_test_evn\AppData\Local\Programs\Python\Python37\
	【C:\Users\linzg_test_evn\AppData\Local\Programs\Python\Python37\】python -m venv .
12.激活环境
	cd Scripts
	activate
13.导入包
	cd C:\Users\linzg_test_evn\Desktop\python离线发布\packages
	pip install --no-index --find-links=C:\Users\linzg_test_evn\Desktop\python离线发布\packages -r packages.txt
	
14.测试启动项目：
	cd C:\Users\linzg_test_evn\Desktop\python离线发布\code\taiji\utilsTest\utils\
	python taiji_count_tool.py

15.编写bat执行脚本
	cd cd C:\Users\linzg_test_evn\Desktop\python离线发布
	md 运行脚本
	cd 运行脚本
	新建txt，输入
	@echo off

	title demo
	cmd "/c c: && cd C:\lin\Scripts && activate && cd 【C:\Users\linzg_test_evn\Desktop\python离线发布\code\taiji\utilsTest\utils\】 && python 【taiji_count_tool.py】 "

	pause
	
	修改名字为：run.bat
	保存后双击运行
	
成功！