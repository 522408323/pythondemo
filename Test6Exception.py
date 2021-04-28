'''

python提供异常机制
AssertionError 断言语句失败异常
AttributeError 访问不存在的对象属性异常
IndexError 索引错误，索引超出范围
KeyError 键异常，键不存在
OSError 秀操作系统异常
OverflowError 数据运算超出最大限制
RuntimeError 一般运行时错误
SyntaxError 语法错误
SystemError 编译器系统错误
TypeError 不同类型间的无效操作
ValueError 传入无效参数
ZeroDivisionError 除数为0错误

'''

#fileName = input("请输入文件名：")
#f = open(fileName)

#dd = {'one':1,'two':2}
#dd['four']

# a = 1+'1'
# a = int('aaa')
# a = 1/0

'''
语法
try:
    需要检测的代码
except Exception[as reason]:
    出现异常后的处理代码
'''
#发生错误
try:
    a = 1/0
    print("结束")
except:
    print("发生错误")
#报错 :[Errno 2] No such file or directory: 'D:\\sss\\a.txt'
try:
    f = open('D:\\sss\\a.txt')
    print(f.read())
    print("结束")
except OSError as reason:
    print('报错 :'+ str(reason))

#这次报错：unsupported operand type(s) for +: 'int' and 'str'
try:
    a = 1+ '1'
    print("结束")
except (OSError,TypeError) as reason:
    print("这次报错："+str(reason))

'''
语法
try:
    需要检测的代码
except Exception[as reason]:
    出现异常后的处理代码
finally:
    最后都会被执行的代码
'''
#发生错误 最后执行
try:
    a = 1/0
    a = a+1
except:
    print("发生错误")
finally:
    print("最后执行")

