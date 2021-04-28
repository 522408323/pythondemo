import os
import time
import pickle
'''
getcwd()：返回当前目录路径
listdir(目录地址) 返回指定目录下的文件或文件夹名称列表
mkdir(path) 创建单层目录，该目录已存在则报错
makedirs(path)创建多层目录，该目录已存在则报错
remove(path) 删除文件
rmdir(path) 删除单层目录，目录下必须为空，否则报错
removedirs(path) 递归删除目录，从子目录到父目录逐层尝试删除，如遇到目录下非空则报错
例如：os.removedirs('D:\\sss\\s') ，先删除s文件夹，再删除sss文件夹
rename(old,new) 重命名
os.curdir 当前目录 .
os.pardir 上一级目录 ..
os.sep 输出操作系统特定分隔符（window下\\ linux下/）
os.linesep 当前平台行终止符 （window下 \r\n linux下\n）
os.name 当前使用的操作系统名字
'''
print(os.getcwd()) # D:\python-workplace\pythondemo
print(os.listdir("D:\\sss"))# ['1.txt', '2.txt', 'd']

print(os.name) # nt
print(os.curdir) # .
print(os.pardir) # ..

'''
os.path下方法：
basename(path) 返回路径中的文件名
dirname(path) 返回文件名前的路径
join(path1,path2,....) 拼接路径
split(path) 分割文件名与路径
splitext(path) 分离文件名与扩展名
getsize(file) 返回指定文件的大小，字节单位
getatime(file) 返回指定文件最近访问时间 （浮点型秒数 ，可用time模块的gmtime()或localtime()函数换算 <记得引用import time>）
getctime(file) 返回指定文件创建时间（浮点型秒数 ，可用time模块的gmtime()或localtime()函数换算 <记得引用import time>）
getmtime(file) 返回指定文件最新修改时间（浮点型秒数 ，可用time模块的gmtime()或localtime()函数换算 <记得引用import time>）

返回true或false的函数方法：
exists(path) 判断文件或目录是否存在
isabs(path) 判断路径是否是绝对路径
isdir(path) 判断路径是否存在且为目录
isfile(path) 判断路径是否存在且为文件
islink(path) 判断路径是否存在且为符号链接

'''

print(os.path.basename("D:\\sss\\1.txt")) # 1.txt
print(os.path.dirname("D:\\sss\\1.txt")) # D:\sss
print(os.path.join('a','b','c')) #a\b\c
print(os.path.split("D:\\sss\\1.txt")) # ('D:\\sss', '1.txt')
print(os.path.split("D:\\sss\\d")) # ('D:\\sss', 'd')
print(os.path.splitext("D:\\sss\\1.txt")) # ('D:\\sss\\1', '.txt')
print(os.path.splitext("D:\\sss\\d")) # ('D:\\sss\\d', '')
print(os.path.getsize("D:\\sss\\1.txt")) # 38
print(os.path.getatime("D:\\sss\\1.txt")) # 1618898756.919341

'''
下面返回结果：
time.struct_time(tm_year=2021, tm_mon=4, tm_mday=20, tm_hour=14, tm_min=5, tm_sec=56, tm_wday=1, tm_yday=110, tm_isdst=0)
解析-->
tm_year	年份 例如 2021
tm_mon	月份 1 到 12
tm_mday	日期 1 到 31
tm_hour	小时 0 到 23
tm_min	分钟 0 到 59
tm_sec	秒   0 到 61 (60或61 是闰秒)
tm_wday	星期  0到6 (0是周一)
tm_yday	一年中的第几天，1 到 366
tm_isdst  是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1
'''
print(time.gmtime(1618898756.919341))
print(time.gmtime(1618898756.919341).tm_year) # 2021

print(os.path.getctime("D:\\sss\\1.txt")) # 1618826918.5350535
print(os.path.getmtime("D:\\sss\\1.txt")) # 1618899131.3753688

'''
pickle

'''
#把列表数据放到二进制文件中
mylist=[1,2.1,'aa',['q','w','e']]
pickle_file=open("D:\\sss\\test3.pkl",mode='wb')
pickle.dump(mylist,pickle_file)
pickle_file.close()
#读取二进制文件列表数据
pp = open("D:\\sss\\test3.pkl",mode='rb')
mm = pickle.load(pp)
print(mm)