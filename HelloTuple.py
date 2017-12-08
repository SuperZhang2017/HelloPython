#tuple数据结构
#1.赋值
tuA=(1,2,(1,2),)
print(tuple('abc'))
#2.下标访问
print(tuA[1])
print(tuA[2][1])
print(tuA[:2])
print(tuA[:3])
print(tuA[1:])
#3.不可变
#tuA[0]=2#error
print(tuA)
print(id(tuA))
tuB=(1,2)
tuB=tuA
print(tuB)
print(id(tuB))
tuB=(2,2)
print(id(tuB))#id()变化，指向不同的对象
#tuB[0]=1  #error，不可改变元祖元素
print(tuB)
#4.删除元祖
#del tuB[0] #error,不可删除元祖中元素
del tuB#删除整个元祖
#5.元祖操作符
t=(1,2,1,)
tt = t * 2#(1,2,1,1,2,1)
print(tt)
print(2 in t)
print((1,2)>(1,0))#true
print((1,2)==(2,1))
print(t[1:])
#6.内建函数
str(t)
print(str(t))
print(len(t))
print(max(t))
print(min(t))
print(list(t))#tuple->list
t+=tt
print(t)

#元祖对象本身不可变，但不代表其包含的可变对象不可变
ttt=([1,2,'a','b'],1,22)
ttt[0][1]=0
print(ttt)



