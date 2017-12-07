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