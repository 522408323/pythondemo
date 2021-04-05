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

'''
break ：跳出循环体
continue : 跳过当前循环，走下一个循环
'''