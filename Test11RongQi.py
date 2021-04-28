'''
容器类型的协议
定制容器不可变的话，只需要定义__len__() 和__getitem__()方法
定制容器是可变的话，除了__len__(),__getitem__()方法外，还需要定义__setitem__() 和 __delitem__()两个方法

__len__(self) 定义当被len()调用时返回容器中元素个数
__getitem__(self,key) 获取容器中指定元素，相当于 self[key]
__setitem__(self,key,value) 设置容器中指定元素 self[key] = value
__delitem(self,key) 删除容器中指定元素，相当于 del self[key]
__iter__(self) 迭代容器中的元素
__reversed__(self) 当被reversed()调用时
__contains__(self,item) 容器是否包含某个元素
'''

class CountList:
    def __init__(self, *args):
        #lambda表达式：[x for x in args] 相当于 for x in args： self.values.append(x)
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)
    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        self.count[item] += 1
        return self.values[item]

co = CountList(1,3,5,7,9)
co2 = CountList(2,4,6,8,10)
print(co.count) # {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
print(co[1]) # 3
print(co.count) #{0: 0, 1: 1, 2: 0, 3: 0, 4: 0}
