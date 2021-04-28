'''
容器类型的协议
定制容器不可变的话，只需要定义__len__() 和__getitem__()方法
定制容器是可变的话，除了__len__(),__getitem__()方法外，还需要定义__setitem__() 和 __delitem__()两个方法

__len__(self) 定义当被len()调用时返回容器中元素个数
__getitem__(self,key) 获取容器中指定元素，相当于
__setitem__(self,key,value) 设置容器中指定元素
'''

