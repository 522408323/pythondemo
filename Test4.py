'''
函数
使用def创建函数方法
def 函数名():
    函数体
调用函数：只需要 函数名()
'''
#无参函数
def ceshi():
    print("第一个函数")

ceshi()
#有一个参函数
def secondFun(name):
    print("name："+name)
secondFun("john")
#有2个参函数
def thirdFun(name1,name2):
    print(name1 + name2)
thirdFun(1,2) # 3
thirdFun("11","22") # 1122
#也可以标注参数名，这样更准确赋值
thirdFun(name1=3,name2=4) # 7
#有返回值的函数
def fourFun(name1,name2):
    return name1 + "==="+name2
print(fourFun("a","b")) #a===b

#函数文档
def aaa():
    '这是aaa的说明文档'
    #这是aaa的注释说明
    print("aaaaaa")
#查看函数文档
print(aaa.__doc__) # 结果：这是aaa的说明文档

#可变参数： *参数名
def test(*params):
    print("参数长度：",len(params))
    if len(params) > 0:
        print("第一个参数：",params[0])
test(1,2,3) #参数长度： 3 第一个参数： 1
test() # 参数长度： 0

#可变参数与固定参数一起使用，记得标记
def test2(*params, exp):
    print("参数长度：",len(params),"exp=",exp)
test2(1,2,3,exp="1111111") # 参数长度： 3 exp= 1111111
#无返回值打印
temp = ceshi()
print(temp) # None ceshi()没有返回值，所以temp默认是None
print(type(temp)) #<class 'NoneType'>
#返回多个值打印
def back():
    return [1,2,3,4]
t = back()
print(t) #[1, 2, 3, 4]

#函数中修改全局变量:global 参数名
index = 1
def test3():
    global index
    index = 10
    print(index)
test3() # 10
print(index)# 10

#嵌套函数
def fun1():
    print("fun1正在被调用")
    def fun2():
        print("fun2正在被调用")
    fun2()

fun1()#fun1正在被调用 fun2正在被调用

#
def funX(x):
    def funY(y):
        return x * y
    return funY
print(funX(5)(6)) # 30 ,funx(5) = funY函数，然后funY(6)
#
def fun11():
    xx = [5]
    def fun22():
            xx[0] *= xx[0]
            return xx[0]
    return fun22()

print(fun11()) # 25

'''
lambda表达式
'''
#示例一
def dd1(x):
    return x + 1
print(dd1(10))

ddd1 = lambda x: x+1
print(ddd1(10))
#示例二
def dd2(x,y):
    return x + y
print(dd2(1,2))
ddd2 = lambda x,y : x + y
print(ddd2(1,2))

'''
filter(function or None, iterable)
过滤出符合条件的元素
如果function为None，则返回为true的元素。
如果function是某个函数，则返回符合该函数结果不为False或0定义的元素
'''
#示例一，将数组中为true的元素过滤出来
a = filter(None,[1,0,False,True])
print(list(a)) # [1, True]

#示例二，将数组中每个元素都赋值给add函数的x得到的计算结果不是0的过滤出来
def add(x):
    return x % 2
b = filter(add,range(10))# range(10)是1到9数组
print(list(b)) # 结果为 [1, 3, 5, 7, 9]

'''
map(func, *iterables) 
将数组中每个元素在函数中处理后展示出来
'''
def add1(x):
    return x + 1
m = map(add1,[1,2,3,4,5])
print(list(m))# 结果为 [2, 3, 4, 5, 6]

'''
字典，映射类型
1.格式：{key:value,key:value,...}
2.使用自带函数dict()
'''
#示例一
dic = {1:'张三',2:'李四'}
print(dic[1])#张三
#示例二
dic = {'one':'张三','two':'李四'}
print(dic['two'])#李四
#示例3 ，使用dict函数，key不能是数字
ccc = dict(a="哈哈", b="呵呵")
print(ccc) # {'a': '哈哈', 'b': '呵呵'}

#示例4
ccc = dict(( ('1','a'),('2','b'),('3','c') ))
print(ccc) #{'1': 'a', '2': 'b', '3': 'c'}

ccc['1'] = "呵呵"
print(ccc) # {'1': '呵呵', '2': 'b', '3': 'c'}

#示例5，获取所有key，打印结果：1 2 3
for key in ccc.keys():
    print(key,end=" ")
#示例6，获取所有value，打印结果：呵呵 b c
for value in ccc.values():
    print(value,end=" ")
print()
#示例6，获取所有元素，打印key和value
for i in ccc.items():
    print(i," ",i[0]," ", i[1])
'''
('1', '呵呵')   1   呵呵
('2', 'b')   2   b
('3', 'c')   3   c
'''
#示例7，获取不存在key的值
print(ccc.get('6'))# None
print(ccc.get('6',"空"))# 空 ，第2个参数为不存在时给定一个默认值

#清空字典
#ccc.clear()

#浅拷贝copy()
ccd = ccc.copy()
print(id(ccd),id(ccc)) # 2861038148480 2861038148608

print(ccc.pop('3')) # c 剔除某个key的元素

#更新或新增某个元素，key存在则更新，key不存在则新增
ccc.update({"2":"111"})
print(ccc) # {'1': '呵呵', '2': '111'}

'''
集合 set 无序，元素不重复
格式：
1:{obj,obj,...}
2:set()
'''
#示例1
n1 = {1,2,3,4}
print(type(n1)) # <class 'set'>
#示例2
n2 = set([1,2,3,4,5])
print(type(n2)) # <class 'set'>
#示例3，元素不重复，无序
n3 = {2,2,3,4,0}
print(n3) #{0, 2, 3, 4}

print(2 in n3) # True 判断集合中是否存在2
# 示例4 ，添加元素，删除元素
n3.add(9)
print(n3) #{0, 2, 3, 4, 9}
n3.remove(9)
print(n3) #{0, 2, 3, 4}

'''
不可变集合 frozen
该集合没有add() remove()等修改操作方法
'''
n4 = frozenset([6,7,8,9])
print(n4) #frozenset({8, 9, 6, 7})

