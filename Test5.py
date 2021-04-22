'''
open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
r : 只读方式打开文件（默认）
w : 写入方式打开文件，会覆盖已存在的文件
x :如果文件已存在，使用该模式打开将发生异常
a : 以写入模式打开，如果文件存在，则在末尾追加写入
b : 以二进制模式打开文件
t : 以文本模式打开（默认）
+ ：可读写模式
U ：通用换行符支持

f.close() 关闭文件
f.read(size=-1)从文件读取size个字符，当为给定size或给定负值时，读取剩余所有字符，然后作为字符串返回
f.readline() 以写入模式打开，如果文件存在，则在末尾追加写入
f.write(str) 将字符写入文件
f.writelines(seq) 向文件写入字符串序列seq, seq 应该是一个返回字符串的可迭代对象
f.seek(offset,from) 在文件中移动文件指针，从from(0代表文件起始位置<默认>，1：代表当前位置，2代表文件末尾) 偏移offset个字符
f.tell() 返回当前在文件中的位置

'''
'''
test.txt内容：
1.那轻脆的铃响，
那秀丽的流苏，
只为佳人那动人的笑靥。
长安初雪后，
那宫阙重楼里，
元宵灯海美如昼。
'''
#因为我的test.txt是utf-8编码，所以我需要设置读取的编码格式为utf8，默认编码格式是cp936
# f = open("D:\\test.txt",encoding='utf8')
# print(f)# <_io.TextIOWrapper name='D:\\test.txt' mode='r' encoding='cp936'>
# print(f.read(5)) # 1.那轻脆 ，获取前5个字符
# print(f.tell()) # 获取当前读取位置，结果：11（按字节算位置），1+1+3+3+3（单个数字或字符为一字节 单个汉字为3字节）
# f.seek(5,0) # 代表从第5个字节开始读
# print("读取3个字符：",f.read(3)) # 结果：轻脆的，上面设置的是从第五个字节开始读，read(3)指的读取3个字符，
#
# f = open("D:\\test.txt",encoding='utf8')
# f.seek(5,0) # 代表从第5个字节开始读
# print("读取一行字符：",f.readline()) # 结果：轻脆的铃响，，上面设置的是从第五个字节开始读，读取一行字符
#
# # for循环读取文件每行数据
# f.seek(0,0) #还原到从第一个字节开始读取
# for line in f:
#     print(line)
'''
打印结果：
1.那轻脆的铃响，

那秀丽的流苏，

只为佳人那动人的笑靥。

长安初雪后，

那宫阙重楼里，

元宵灯海美如昼。

'''

f = open("D:\\test.txt",mode='w',encoding='utf8')

f.write("2:一手莲灯，\n一个心愿，\n一柄萤扇，\n一丝心凉，\n一壶美酒，\n一滴泪水。\n轻迈脚步，\n游走人群，\n牵着孤独，\n看海棠花瘦。")
'''
test.txt内容被覆盖为下面内容：
2:一手莲灯，
一个心愿，
一柄萤扇，
一丝心凉，
一壶美酒，
一滴泪水。
轻迈脚步，
游走人群，
牵着孤独，
看海棠花瘦。
'''
#当前文件末尾追加内容 最末尾一行：看海棠花瘦。123123313131313方法撒发发发发发发
f.writelines("123123313131313")
f.writelines("方法撒")
f.writelines("发发发发发发")
f.close()
'''
一个小实例，
test2.txt的内容：
A：您好
B：您有什么事
A：我想问个路
B：您打算去哪

使用语法：
split(指定分隔符,<分割次数,默认为 -1,即分隔所有>)

效果如下：
a.txt:
您好
我想问个路

b.txt:
您有什么事
您打算去哪
'''
f = open("D:\\test2.txt",mode='r',encoding='utf8')

file_a = open("D:\\a.txt",mode='w',encoding='utf8')
file_b = open("D:\\b.txt",mode='w',encoding='utf8')
for each in f:
    [role,content] = each.split("：",1)
    if role == 'A':
        file_a.writelines(content)
    elif role == 'B':
        file_b.writelines(content)

file_a.close()
file_b.close()
f.close()
print("分割结束")


'''
with 可以自动关闭文件流,不用再调用close()方法
'''
with open("D:\\a.txt",mode='r',encoding='utf8') as k:
    for line in k:
        print(line)
