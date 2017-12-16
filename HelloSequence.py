#常用序列式数据类型：list、tuple、string
#1.list
#1.1创建列表、赋值
li = [123,'abc',7.89,[1,2,3]]
print(li)
liA =list('abc')
print(liA)
print(tuple('abc'))
#1.2访问列表值，下标访问
print(li[3][1])
print(li[:3])
#1.3更新列表
print(li[2])
li[2]=1000
print(li[2])
li.append(765)
print(li)
#在index前插入
li.insert(0,'efg')
print(li)
li.remove('efg')
print(li)
print(li.index('abc'))
ll=li.copy()
print(ll)
c=li.count('abc')
print(c)
print(li.pop(3))
print(li)
print(li.clear())
#del li[0]
print(li)
del liA[0]
print(liA)
liA.append('a')
print(liA)
liA.reverse()
print(liA)
#*重复操作符
A=[1,2,3]
B= A*2
print(B)
print(len(A))
#重要：列表推导式
m=[x%2 for x in [1,2,3,4]]
print(m)
n=[x*2 for x in range(10) if x%2==0]
print(n)

#常见列表内建函数
#append/count/extend/index/insert/pop/remove/sort/reverse
A.append(4)
print(A.count(1))
print(A.extend(B))#None
print(A)
print(A.index(2,6,len(A)))#返回第一个值为2的索引值
A.reverse()#翻转
print(A)

#排序
A.sort()
print(A)
#自定义排序
M=[('a',1),('b',-1)]
M.sort(key=lambda x:x[1])
print(M)

M.sort(key=lambda x:x[1],reverse=True)
print(M)
M.sort(key=lambda x:x[1])
print(M)

#2.map()/filter()/reduce()与lamada连用
li = [2,3,4,5,10,2,-6]
re = map(lambda x:x*x,li)
print(list(re))

res = filter(lambda x:x%2==0,li)
print(list(res))

from functools import reduce

resu = reduce(lambda x,y:x-y,li)
print(resu)

#有初始值
resu = reduce(lambda x,y:x*y,li,0)
print(resu)

#3.多重赋值
a, b = 1, 2
print(a)
print(b)
#赋值变量个数一致，不然报错
a, b, c = 3, 2,1#error not enough values to unpack
print(a)
print(b)
print(c)

a,b = 3,2#error too many values to unpack
print(a)
print(b)

#4.变量交换：相比java 写法简洁
a = 1
b = 2

a,b = b,a
print(a)#2
print(b)#1

c = 3

a,b,c = c,a,b
print(a)
print(b)
print(c)