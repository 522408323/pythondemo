# if elif(else if)
# a = int(input("输入一个数字："))
# if a > 10:
#     print("大于10")
# elif a > 5:
#     print("大于5小于10")
# else:
#     print("小于=5")

# 三元操作符
x,y = 4,5
if x < y:
    s = x
else:
    s = y
#上面改为：
s = x if x < y else y

#断言 assert 后面条件为false时 报错：AssertionError
#assert 1 > 2 # 报错AssertionError

'''
while 条件:
    循环体
'''

'''
for 目标 in 表达式:
    循环体
'''
a = "study"
for i in a:
    print(i,end=" ") # s t u d y
print()
#数组 [对象，对象]
b = ['a','b','c','d','e']
for e in b:
    print(e,len(e), end=" ")
print()
'''
结果：
b 1
c 1
d 1
e 1
'''
print("hello"+"world") #helloworld
print("hello","world") #hello world ,逗号表现效果为空格形式

'''
range([start,] stop[, step=1])
3个参数，start和step是可选的， stop是必填项
step=1: 第三个参数默认值为1
作用： 生产一个从start参数的值开始到stop参数的值结束的数字序列
3个参数都只能是integer数字，整形数字
最后一个数是stop-step，不是stop
假如start 大于等于stop 则不展示任何数字
step的值不能=0 ，会报错：ValueError: range() arg 3 must not be zero
step小于0的话也不展示任何数字
'''
r = range(0,5,1)
for i in r:
    print(i,end=" ")
print()
'''
break ：跳出循环体
continue : 跳过当前循环，走下一个循环
'''

'''
数组
'''
arr = ['张三','李四','王五']
num = [1,2,3,4]
mix = ['张三',1,[1,2,3],3.14]
empty = []
print(len(empty)) # 0
#向数组添加元素 append(只能一个元素)
empty.append('哈')
print(len(empty)) # 1

# 向数组扩展另一个数组 extend(数组)
ext = ['a','b','c',1]
empty.extend(ext)
print(len(empty)) # 5

#插入一条元素到指定位置 insert(下标数，元素)
empty.insert(1,'s') #结果empty为：['哈','s','a','b','c',1]

#从数组中获取元素
print(empty[1]) #根据下标获取元素，此处为s

#从数组中删除元素，删除不存在的元素会报错
empty.remove('s') #结果empty为：['哈','a','b','c',1]

#del 删除某个元素，删除整个数组
del empty[0] # 结果empty为：['a','b','c',1]
for i in empty:
    print(i,end=" ")
print()
#del empty #结果empty就未赋值，不能使用，会报错NameError: name 'empty' is not defined

#pop() 删除数组末尾元素 pop(下标数)删除指定位置元素,都会返回删除的元素
print(empty.pop()) #1 ,此时empty=：['a','b','c']
print(empty.pop(0))#a ,此时empty=：['b','c']

#复制数组一部分元素 empty[开始下标（包含）:结束下标（不包含）]
new = empty[0:1]
print("new:",new) # ['b']

empty[:1] #等价于empty[0:1],得到 [b]
empty[1:] #等价于empty[1:2],得到 [c]
empty[:]  #等价于empty[0:2],得到全部数组元素[b,c]

#数组合并
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print("list3:",list3)# list3 = [1, 2, 3, 4, 5, 6]
list4 = list1 + ['sss']
print("list4:",list4)#list4 = [1, 2, 3, 'sss']

list2 *= 2
print("list2:",list2)# [4, 5, 6, 4, 5, 6]

#包含in，不包含not in
print(1 in list1) # True
print(4 not in list1) # True

#获取二维数组中的元素
er = [1,[3,4],5,1,'ee']
print(er[1][0]) # 3

#count(元素值) 获取相同元素的个数
print(er.count(1)) # 2

#获取数组下标 index(元素值),元素有重复的话取第一个下标数
print(er.index(1)) #0

#倒序reverse()
er.reverse()
print("er.reverse:",er)# ['ee', 1, 5, [3, 4], 1]

#数字排序 正序：sort() 倒序： sort(reverse=True)
er = [4,2,6,3,7,1]
er.sort()
print("er.sort:",er)# [1, 2, 3, 4, 6, 7]
er.sort(reverse=True)
print("er.sort(reverse=True):",er)# [7, 6, 4, 3, 2, 1]

#元组，和数组类似,但是不可修改，可以通过截取和拼接更改
t = (1,2,3,4,5)
print(t[2]) # 3
t[2:] # 3,4,5
t[:3] # 1,2,3
t[:]  # 1,2,3,4,5
# t[0] = 9 会报错，不支持修改

t = () #初始化元组
'''
t = (1) # 只有一个元素
type(t) # 得到的是int 类型 ，不是元组tuple类型
t = (1,) # 这才是元组
t = 1,2,3 #这个也是元组类型，逗号是关键
'''
tt1 = (1)
print(type(tt1)) # <class 'int'>
tt2 = (1,) # 也可以 tt2 = 1,
print(type(tt2)) # <class 'tuple'>
tt3 = 1,2,3
print(type(tt3)) # <class 'tuple'>
#元组拼接
tt4 = tt3 + (4,5,)
print("tt4:",tt4) # 1 2 3 4 5 <class 'tuple'>
print(type(tt4)) # 1 2 3 4 5 <class 'tuple'>
# 字符串操作
str1 = "hello world"
print(str1[:5]) #字符串截取 hello

# 第一个字母大写，capitalize()
print(str1.capitalize()) # Hello world

# 全部小写 casefold()
ss = "AAA"
print("casefold：",ss.casefold())# aaa
print("isalnum：",ss.isalnum()) # 至少一个字符，且都是字母或数字则True ,否则false
print("isalpha：",ss.isalpha()) # 至少一个字符，且都是字母则True ,否则false
print("isdecimal：",ss.isdecimal()) # 字符串值包含十进制数字则返回true,否则false
print("isdigit：",ss.isdigit()) # 字符串只包含数字则返回True,否则false
print("isnumeric：",ss.isnumeric()) # 字符串只包含数字字符则True,否则false
y = " abcba ddd"
print("lstrip：",y.lstrip()) # 去掉左边空格
print("rstrip：",y.rstrip()) # 去掉右边空格
print("strip：",y.strip()) # 去掉两边空格
print("replace：",y.replace("a","b")) # 替换符合条件的所有字符串
print("replace（old,new,num）：",y.replace("a","b",1)) # 1代表替换次数,如果有多个相同元素，只替换前N个，此处是前1个
print("split：",y.split()) # ['abcba', 'ddd']
print("split(str)：",y.split("b")) # [' a', 'c', 'a ddd']
print("split（str,num）：",y.split("b",1)) #[' a', 'cba ddd'] ,1代表分1次

#字符串格式化
f = "{0} love {1}"
print(f.format("I","you")) # I love you
f = "{a} love {b} !"
print(f.format(a="I", b="you"))# I love you !
f1 = "{0:.1f}"
print(f1.format(27.123)) # 27.1 ，0是变量,.1f表示保留1位小数
'''
%c 格式化字符及其ASCII码 %97 = a
%s 格式化字符串
%d 格式化整数
%o 格式化八进制数
%x 格式化16进制
%X 格式化16进制（大写）
%f 格式化浮点数，可指定小数位数
%e 科学技术法
%g 自动判断使用%f或%e
m.n m是显示的最小总宽度，n是小数后的位数
- 用于左对齐
0 显示的数字前面填充0代替空格

\' 单引号
\" 双引号
\a 系统响铃声
\b 退格符
\n 换行符
\t tab
\r 回车符
\f 换页符
\\ 反斜杠
'''

