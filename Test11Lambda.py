'''
lambda表达式,可以减少冗余代码
格式 <函数名> = lambda <参数>：<表达式>
等价于 def <函数名>（参数）：
        <函数体>
        return <返回值>
'''
#示例一
def sum1(x):
    return x
print(sum1(5)) # 5
##lambda表达式改为
sum1 = lambda x:x
print(sum1(5)) # 5
#示例二
def sum2(x,y):
    return x + y
print(sum2(4,5)) # 9
#lambda表达式改为
sum22 = lambda x,y:x+y
print(sum22(4,5)) # 9

#示例3
def sum3(x,y,z):
    return x + y + z
print(sum3(4,5,6)) # 15
#lambda表达式改为
sum33 = lambda x,y,z:x+y+z
print(sum33(4,5,6)) # 15

#range(n) [0,.....,n-1]
for i in range(6):
    print(i,end=' ')
print("")
#映射 map(function,iterable,....) 第一个参数是函数方法，第二个参数是一个或多个序列,
#注意：函数方法的参数个数与序列个数保持一致，否则会报错
def s(x):
    return x * 2
print(list(map(s,range(6))))#[0, 2, 4, 6, 8, 10]
#可以合并为
print(list(map(lambda x:x*2,range(6)))) #[0, 2, 4, 6, 8, 10]
#也可以合并为
print([x * 2 for x in range(6)]) # [0, 2, 4, 6, 8, 10]

def s2(x,y):
    return x * y
#print(list(map(s2,range(6)))) 该代码会报错，原因是缺少一个序列为y参数赋值

#多个序列元素个数不一致，取最小个数的计算结果
print(list(map(s2,range(6),range(7)))) # [0, 1, 4, 9, 16, 25]
print(list(map(s2,range(7),range(6)))) # [0, 1, 4, 9, 16, 25]

#如果map第一个参数不传入任何函数名，则相当于将多个序列相同位置的元素分别归并到一个元组中
#print(list(map(None,range(6))))

#类型转换
print(list(map(int,(1,2,3)))) # [1, 2, 3] ，元组转数组
print(list(map(int,'12345'))) #[1, 2, 3, 4, 5] 字符串转数组
print(list(map(int,{1:'a',2:'b',3:'c'}))) # [1, 2, 3] ，字典的key转数组