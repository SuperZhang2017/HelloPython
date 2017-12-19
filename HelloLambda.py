#匿名函数lambda
#lambda 表达式返回可调用的函数对象
def true():
    return True
#等价于
A = lambda :True
print(A)
print(A())
#=======================
def add(x,y=2):#带有默认参数
    return x+y

print(add(1))
print(add(1,6))

B = lambda x,y=2:x+y
print(B(1))
print(B(1,6))
#=======================
def show(*z):
    return z
print(show(1,2,3))

C = lambda *z: z
print(C([1,2,3]))
print(C(1,2,3))

D = lambda **z: z
print(D(a=1,b=2))

E = lambda x: x**2
print(E(5))

#=========复习：filter map reduce 与lambda 连用=============
#filter(boolfun,seq)
#map(fun,seq)
#reduce(fun,seq,initVal)

#=======filter():filter()为已知的序列的每个元素调用给定的布尔函数，调用中，返回值为非零的元素将被添加至一个列表中==================
#filter(function or None, sequence) -> list, tuple, or string
#function是一个谓词函数，接受一个参数，返回布尔值True或False。
#如果function参数为None，返回结果和sequence参数相同
def odd(n):
    return n % 2

seqA = (1,2,3,4,5,6)

reA = filter(odd , seqA)
print(type(reA))
print(list(reA))

print(list(filter(None,seqA)))

#方法1.===================
from random import randint
se = []
for e in range(0,101):
    se.append(e)
print(se)
print(list(filter(lambda n:n % 2 == 0, se)))
#方法2.===================
print(list(x for x in se if x % 2 == 0 ))
#方法3.===================
from random import randint as ri
print(list(x for x in range(101) if x % 2 ==0))

#========== map():map()将函数调用映射到每个序列的对应元素上并返回一个含有所有返回值的列表=================
#map(function, sequence[, sequence, ...]) -> list
l1 = [1,2,4]
l2 = ['a','b','c']
reC = list(map(lambda x,y: x*y, l1, l2))
print(reC)
reD = list(map(lambda x: x**2,l1))
print(reD)

#========== reduce():reduce函数会对参数序列中元素进行累积,返回value值============================
#reduce(function, sequence[, initial]) -> value
#注意function函数不能为None。
#unction参数是一个有两个参数的函数
#reduce依次从sequence中取一个元素，和上一次调用function的结果做参数再次调用function。
#第一次调用function时，如果提供initial参数，会以sequence中的第一个元素和initial作为参数调用function，否则会以序列sequence中的前两个元素做参数调用function。
from functools import reduce
m = reduce(lambda x,y:y,l1)
n = reduce(lambda x,y:x,l1)
print(m)#4
print(n)#1
print(m==n)#False

mn = reduce(lambda x,y:x**2+y,l1)
print(mn)#13




