'''
模块 指的就是一个python文件
可以把三方或自定义的模块放到site-packages文件夹下，也可以添加指定的路径,如下
import sys
sys.path.append("模块所在目录路径");

创建包，就是在指定目录下新加一个文件夹M，里面有模块test.py,引用模块test.py时
import M.test
'''
import sys
sys.path.append("XXXXX");


