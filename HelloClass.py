#class 类的定义
# 1.简单类
class simpleClass:
    """a simple class definition"""
    a = 100
    def fu(self):
        return "hello world!"

c = simpleClass()#创建对象，分配内存
print(c.__doc__)
print(c.a)
print(c.fu())

# ======初始化类__init__()=============
class Hello:
    """init class"""
    m, n = 1, 2
    def __init__(self):
        self.m = 100
        self.n = 200

    def __init__(self,m,n):
        self.m = m
        self.n = n


#d = Hello()
# print(d.m)
# print(d.n)

e = Hello(3,4)
print(e.n)
print(e.m)
#给该对象增加属性counter,属于当前对象
e.counter = 1
print(e.counter)
# del e.counter#删除对象counter属性
f = Hello(7,8)
# print(f.counter)#f指向的对象无counter属性
f = e
print(f.m)#3

# ================
class CAT:
    def __init__(self,name):
        self.name = name
        self.tricks =[]

    def add(self,m):
        self.tricks.append(m)


cc = CAT("cat")
dd = CAT("dog")
cc.add("little cat")
dd.add("big dog")

print(cc.tricks)
print(dd.tricks)

#=================function defined outside
def f(self, x,y):
    return min(x,y)

class jj():
    f1 = f
    def g(self):
        return "hello python"
    h = g

ff = jj()
print(ff.f1(1,2))
print(ff.g())

#================继承
class animal:
    def __init__(self,iterable):
        self.items=[]
        self.__update(iterable)

    def update(self,iterable):
        for i in iterable:
            self.items.append(i)
    __update = update

class dog(animal):
    def update(self,keys,values):
        for items in zip(keys,values):
            self.items.append(items)

ddd = dog([1,2,3])
print(ddd.items)
ddd.update([1,2,3],[5,6,7])
print(ddd.items)

ee = animal([1,2,3])
print(ee.items)
ee.update([4,5,6])
print(ee.items)
# ee.__update([7,8,9])
print(ee.__doc__)
print(ee.__dict__)
print(ee.__class__)
print(ee.__hash__())


#generator 生成器
def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

datas = "hello world"
print(list(reverse(datas)))

#复习，生产器，迭代
# 1.
sum(i*i for i in range(10))
#2.
xx = [1,2,3]
yy = [4,5,6]
re = sum(x*y for x,y in zip(xx,yy))
res = sum(x*y for x in xx for y in yy)
print(re)#对应相乘后相加
print(res)#
print(re == res)#false
#3
class student():
    def __init__(self,gpa,name):
        self.gpa = gpa
        self.name = name
student1 = student(100,'kitty')
student2 = student(99,'john')
graduates =[]
graduates.append(student1)
graduates.append(student2)
#
# graduates.pop(student1)
# graduates.append(student1)
valedictorian = max((student.gpa, student.name) for student in graduates)

print(valedictorian)









