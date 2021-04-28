'''
类，对象，属性
'''
class Dog:#首字母大写
    #属性
    color = 'white'
    weight = 90
    legs = 4
    name = ''
    #初始化对象属性, init方法不能有返回值
    def __init__(self,name):
        self.name = name
    #定义私有变量，只需要变量名前加__(两个下划线)，不加的话就是公有变量，可以被访问
    __age = 20
    #外部读取私有变量数据
    def getAge(self):
        return self.__age

    #方法
    def eat(self):
        print(self.name,"正在吃饭。。。")

#如果没有__init__初始化方法 ,则声明对象 tt = Dog()
tt = Dog('哈利')
print(tt.color)
tt.eat()
print(tt.getAge())

#父类方法
class Parent:
    def say(self):
        print("父类方法")
#子类继承父类：Child继承Parent
class Child(Parent):
    pass # pass 不做任何事情，是空语句，是为了保持程序结构的完整性。

class Son(Parent):
    def say(self):
        print("子类方法")
p = Parent()
p.say()
c = Child()
c.say()
s = Son()
s.say()

import random as r
class Cat:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print("我的位置是：x=%d y= %d" % (self.x,self.y) )
'''
子类重写父类init方法
如果子类调用父类move方法且不报错，需要把x,y的赋值代码加上，有两种方式：
1.调用父类的init方法
2.使用super方法
'''
class ChildCat(Cat):
    def __init__(self):
        #Cat.__init__(self)
        super().__init__()
        self.age = 10
    def show(self):
        print("这辆车使用%d年" % self.age)
class ChildCat2(Cat):
    def eat(self):
        print("我正在吃晚饭")
cat = Cat()

cat.move()

cc = ChildCat()
cc.show()
cc.move()

#多重继承
class C(ChildCat,ChildCat2):
    pass

c = C()
c.show()
c.eat()
#变量名和方法名如果同名，则方法报错


'''
issubclass(a,b) a是否是B的子类，返回True或false,(注意：Cat类也是Cat类本身的子类) 
isinstance(a,b) a是否是B的实例对象，返回True或false
hasattr(a,x) x是否是a对象的属性
getattr(a,x[,default]) 获取a对象的x属性值，属性不存在则取default默认值
setattr(a,x,value) 给a对象的x属性赋value值
delattr(a,x) 删除a对象的x属性，如果属性不存在则报错
'''
class A:
    pass
class B(A):
    pass
class C:
    def __init__(self,x):
        self.x = x
print("issubclass(A,B):",issubclass(A,B)) # False , A不是B的子类
print("issubclass(B,A):",issubclass(B,A)) # True , B是A的子类
print("issubclass(B,B):",issubclass(B,B)) # True , B是B的子类

a = A()
print('isinstance(a,A):',isinstance(a,A)) # True，a是A类的实例对象
c = C(0)
print(hasattr(c,'x')) # True x是c的属性名

'''
property(fget=None, fset=None, fdel=None, doc=None):
'''
class CC:
    def __init__(self,size=10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self,v):
        self.size = v
    def delSize(self):
        del self.size
    x = property(getSize,setSize,delSize)

#正常获取size值
cc = CC()
print(cc.getSize())
#另一种获取size值
print(cc.x)

#正常修改size值
cc.setSize(20)
print(cc.size)
#另一种修改size值
cc.x = 30
print(cc.size)

#正常删除size
#cc.delSize()
#print(cc.size) # AttributeError: 'CC' object has no attribute 'size'
#另一种删除size
#del cc.x
#print(cc.size) # AttributeError: 'CC' object has no attribute 'size'

'''
__new__(cls[,...])
__del__() 
int.__add__() 加法
int.__sub__() 减法
'''
class TryInt(int):
    def __add__(self, other):
        return self + other

q = TryInt(3)
w = TryInt(5)
#实验：q + w 这个结果是报错的： RecursionError: maximum recursion depth exceeded
#原因是 return self + other 属于对象相加，q + w 就会无限调用重写的__add__方法

#改进
class TryInt2(int):
    def __add__(self, other):
        #另一种正确写法 return int(self) + int(other)
        return int.__add__(self,other)
qq = TryInt2(3)
ww = TryInt2(5)
print('qq + ww = ',qq + ww) # qq + ww =  8，return后面直接调用父类int的add方法，不会调用TryInt2()中的add方法，不会无限循环

#=================================================
'''
类的部分内置方法
__getattr__(self,name) 当用户试图获取一个不存在的属性时会自动调用该方法
__getattribute__(self,name) 当该类的属性被访问时会自动调用该方法，优先这个方法，当找不到属性时会调用getattr方法
__setattr__(self,name,value) 当一个属性被赋值时会自动调用该方法
__delattr__(self,name) 当一个属性被删除时会自动调用该方法
'''
class AA:
    def __getattribute__(self, item):
        print("__getattribute__")
        return super().__getattribute__(item)
    def __getattr__(self, item):
        print("__getattr__")
    def __setattr__(self, key, value):
        print("__setattr__")
        super().__setattr__(key,value)
    def __delattr__(self, item):
        print("__delattr__")
        super().__delattr__(item)

aa = AA()
aa.x
'''
上面结果：
__getattribute__
__getattr__
'''
aa.x = 1
'''
上面结果：
__setattr__
'''
aa.x
'''
上面结果：
__getattribute__
'''

#=========================================================
'''
描述器Descriptor，拥有下面方法的类只能是其实例属于其他类属性的时候生效
__get__(self, instance, owner)
__set__(self, instance, value)
__delete__(self, instance)
'''
class BB:
    def __get__(self, instance, owner):
        print("get...",self,instance,owner)
    def __set__(self, instance, value):
        print("set...",self,instance,value)
    def __delete__(self, instance):
        print("delete...",self,instance)
class Test:
    x = BB()

test = Test()
#下面结果：get... <__main__.BB object at 0x0000028746FD70A0> <__main__.Test object at 0x0000028746FD4FA0> <class '__main__.Test'>
test.x
#下面结果：set... <__main__.BB object at 0x0000028746FD70A0> <__main__.Test object at 0x0000028746FD4FA0> abc
test.x = 'abc'
#下面结果：delete... <__main__.BB object at 0x0000028746FD70A0> <__main__.Test object at 0x0000028746FD4FA0>
del test.x

#============================================
print("======================================")
'''
模拟property实现代码
'''

class MyProperty:
    def __init__(self,fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        #下面一行代码等同于 MyProperty实例对象.getSize(instance) ,其中instance代表类CCC实例对象ccc
        #关键是外部参数传入的是函数方法，相当于MyProperty中也有一个getSize(object)方法，只不过object对象对应的是CCC的实例对象
        print("Property get",self,instance,owner)
        return self.fget(instance)
    def __set__(self, instance, value):
        print("Property set",self,instance,value)
        self.fset(instance,value)
    def __delete__(self, instance):
        print("Property delete",self,instance)
        self.fdel(instance)

class CCC:
    def __init__(self,size=10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self,v):
        self.size = v
    def delSize(self):
        del self.size
    x = MyProperty(getSize,setSize,delSize)

ccc = CCC()
print(ccc.x)
ccc.x = 18
print(ccc.x)

#============================================
print("======================================")
