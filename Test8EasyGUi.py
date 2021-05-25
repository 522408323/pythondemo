'''
图形用户界面入门：EasyGUI
官网下载地址：https://sourceforge.net/projects/easygui/files/0.97/
打开页面后选中easygui-0.97.zip，也可以从上一级重新选择版本
=============================
安装包解压之后，将安装包里面的easygui.py复制粘贴到安装python的site-packages文件夹下（例如 D:\tools\python392\Lib\site-packages）
也可以直接放到Lib文件夹下（例如 D:\tools\python392\Lib），都能被代码引用，site-packages主要是放三方模块的，更倾向于放到这。
之后在python中代码测试：
import easygui
easygui.msgbox('This is a basic message box.','Title Goes Here')
其他安装说明：
第一步：解压easygui-0.97.zip
第二步：使用命令窗口切换到easygui-docs-0.97的目录下。
第三步：在windows下执行  C:Python34python.exe setup.py install
　　　　在Linux或Mac下执行  sudo /usr/bin/python34 setup.py install
　　　（命令的前面部分是python程序在电脑上的安装路径，自行进行修改）
=============================
安装教程参考文章：https://blog.csdn.net/qq_31163325/article/details/74626417
使用教程参考文章：
http://www.manongjc.com/article/7054.html
https://blog.csdn.net/mingqi1996/article/details/81272621
官方使用教程（英文）：http://easygui.sourceforge.net/tutorial.html
某视频博主小甲鱼编写教程（中文，貌似需要注册且付费）：https://fishc.com.cn/thread-46069-1-1.html
====================================
除了import easygui导包形式之外，还有一种from easygui import *
这种形式可以不加前缀easygui.
例如：
from easygui import *
msgbox('This is a basic message box.','Title Goes Here')

'''
#第一种导包形式
#import easygui
#easygui.msgbox('这是message box.','这是标题')

#第二种导包形式（出现同名自定义的函数会串方法，容易出问题）
#from easygui import *
#msgbox('这是message box.','这是标题')

#第三种导包形式(推荐，简化名称)
import easygui as g
#g.msgbox('这是message box.','这是标题')


#第一个例子
import sys

# while 1:
#     g.msgbox("欢迎进入第一个界面")
#     choice = g.choicebox('请选择一个爱好','互动界面',['看电视','看电影','看小说','看动漫'])
#
#     g.msgbox('你的选择是：'+str(choice),'结果')
#     if g.ccbox('你希望重新再开始么？','请选择'):#ccbox 展示 continue/cancel两个按钮
#         pass#选择继续
#     else:
#         sys.exit(0)#选择结束

'''
修改默认配置
打开site-packages文件夹下的easygui.py，
可以修改字体：
PROPORTIONAL_FONT_FAMILY = ("MS", "Sans", "Serif")
改为：PROPORTIONAL_FONT_FAMILY = ("微软雅黑") ，前提你的电脑系统中有这个字体才可以有效
可以修改弹出框尺寸，例如choice选择框：
def _ _choicebox下边的root_width=int((screen_width * 0.8))和root_height=int((screen_height * 0.5))
分别改为root_width=int((screen_width * 0.4))和 root_height=int((screen_height * 0.25))
'''

'''
实现一个填写信息界面
'''
# import easygui as g
# msg = "请填写以下联系方式"
# title = "账号中心"
# fieldNames = [' *用户名',' *真实姓名',' *固定电话',' *手机号码']
# filedValues = []
# filedValues = g.multenterbox(msg,title,fieldNames)
#
# while 1:
#     if filedValues == None:
#         break
#     errMsg = ""
#     for i in range(len(filedValues)):
#         option = fieldNames[i].strip()
#         if filedValues[i].strip() == "" and option[0] == "*":
#             errMsg +=('[%s]为必填项。\n\n' % fieldNames[i])
#     if errMsg == "":
#         break
#     filedValues = g.multenterbox(errMsg,title,fieldNames,filedValues)
# print("用户资料如下：%s" % str(filedValues))

'''
提供一个文件夹浏览框，让用户选择需要打开的文本文件，打开并显示文件内容
'''
import easygui as g
import os

filePath = g.fileopenbox(default="*.txt")
with open(filePath) as f:
    title = os.path.basename(filePath)
    msg = "文件【%s】的内容如下：" % title
    text = f.read()
    g.textbox(msg,title,text)