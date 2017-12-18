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

B= lambda x,y=2:x+y
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

def odd(n):
    return n % 2

seqA = (1,2,3,4,5,6)

reA = filter(odd , seqA)
print(type(reA))
print(list(reA))

#方法1.===================
from random import randint
se = []
for e in range(0,101):
    se.append(e)
print(se)
print(list(filter(lambda n:n % 2==0, se)))
#方法2.===================
print(list(x for x in se if x%2==0 ))
#方法3.===================
from random import randint as ri
print(list(x for x in range(101) if x % 2 ==0))








