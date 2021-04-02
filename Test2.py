import random

# s = random.randint(1,10)
#
# temp = input("猜一下数字:")
# guess = int(temp)
# while guess != s:
#     temp = input("重新猜一下数字:")
#     guess = int(temp)
#     if guess == s:
#         # 字符与数字拼接输出用逗号，字符与字符拼接用+ 或逗号
#         print("猜对了,答案是：",s)
#     else:
#         if guess > s:
#             print("猜大了")
#         else:
#             print("猜小了")
# print("猜对了,答案是：",s)
# print("结束了")

#数值类型 整形，布尔类型，浮点型
#科学计数法 1.5e4 代表1.5 * 10的4次方 = 15000
#类型转换：int() ,float(), str()
#指出变量类型 type(变量)
# a = 3
# print(type(a)) # <class 'int'>
# #isinstance(变量,猜想的数据类型) 返回true 或false
# print(isinstance(a,str)) # False
# print(isinstance(a,int)) # True


# 算术符号
a = 1
a += 1
print(a) # 2
a = 3
a -=2
print(a) # 1
#*乘法
a = 2
a *= 10
print(a) # 20
#/除法
a = 4
a /= 3
print(a) #1.3333333333333333
# //除法取整数结果
a = 3
a //= 2
print(a) #1
# //除法取整数的小数结果
a = 3.0
a //= 2
print(a) #1.0
# %除法求余数
a = 3
a %= 3
print(a) # 0
# ** 求幂次
a = 3
a = a ** 2
print(a) # 9 = 3的2次幂

# 逻辑操作符 and or not
#优先级运算 幂运算 > 正负号 > 先乘除后加减 > 比较操作符 > 逻辑操作符，有括号优先

print(not 1>2) # True




