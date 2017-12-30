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


# ============imporve==================
# 私有函数
#
# 如果成员函数或成员变量以双下划线__开始，表示private。不以双下划线开始命名的是公胡成员。python中没有类的保护成员。
#
# 继承：
#
# 继承时成员特性：
#
# 对于类的成员，在子类中可以通过父类.变量名或者子类.变量名来访问，是相同的。
# 对于对象的成员，在子类中通过self.变量名来访问。访问不属于这个类的私有成员“_classname__method”或“_classname__variable”
# 继承时方法的特性：
#
# 生成子类的构造函数的时候，不会自动调用父类的构造函数，你必须手动调用它。同时，在对象释放的时候，同样要手动调用析构函数。
# 子类的构造函数和析构函数可以不定义，如果不定义的话，这会调用基类的构造和析构函数。
# Python不存在动态绑定和静态绑定。这一点和c++不同。
# 如果基类有一个public函数，子类中重新定义一个和他名称相同，子类覆盖父类函数，python中没有函数重载，一个函数名只能对应一个函数。

class A(object):
    a = 10
    def tell(self):
        print('A tell')
        self.say()

    def say(self):
        print('A say')
        self.__work()

    def __work(self):
        print('A work')

class B(A):
    def tell(self):
        print('B tell')
        self.say()
        super(B,self).say()
        A.say(self)

    def say(self):
        print('B say')
        self.__work()

    def __work(self):
        print('B work')
        self.__run()

    def __run(self):#private method
        print('B run')

b = B()
c = b.tell()
#B tell   B say  B work  B run  A say A work A say A work

# print(c)

class A(object):
    """test extend"""
    a = 10
    def tell(self):
        print('A tell')
        self.say()

    def say(self):
        print('A say')
        self.work()

    def work(self):
        print('A work')

class B(A):
    def tell(self):
        print('B tell')
        self.say()
        super(B,self).say()
        A.say(self)
        super().work()
    def say(self):
        print('B say')
        self.work()

    def work(self):
        print('B work')
        self.run()

    def run(self):#public method
        print('B run')

d = B()
e = A()
d.tell()#公有方法，子类重写（override），无函数重载, 若是私有方法（__开始的方法），则子类不能override 父类对应的方法
print(d.a)
print(e.a)
print(d.a == e.a)
#B tell  B say B work  B run A say B work B run  A say() B work B run A work()

#查看类里包含的属性：1.dir() 2.__dict__
# 1.dir()
li = dir(A)
print(li)
# 2.__dict__
li = A.__dict__
print(dict(li))
print(A.__dict__)#类A的属性（字典）
print(A.__doc__)#类A的文档字符串
print(A.__name__)#类A的名字
print(A.__bases__)#类A的所有父类构成的元祖
print(A.__module__)#类A定义所在的模块
print(e.__class__)#类A对应类

#注：__name__常用于类型对象，如内建类型
print(type(3.1243).__name__)#float
print(type('werqwr').__name__)#str

#注：__dict__
# 1.访问一个类的属性时候，python解释器会先搜索字典（__dict__）以得到想要的属性。
# 2.如果在__dict__没有找到，将会在基类的字典中进行搜索，采用"深度优先搜索"顺序
# 3.基类集合的搜索是按照顺序的，从左到右，按其在类定义时，定义父类参数时的顺序
# 4.对类的修改仅会影响到此类的字典，基类的__dict__属性不会被改动的

#注：__module__
#1.5版本引入，类名完全有模块名所限定

from functools import reduce

print(reduce.__module__)
print(reduce.__name__)
print(reduce.__doc__)
print(type(reduce))
print(reduce.__class__)
print(reduce.__init__())

print(map.__dict__)
print(map.__module__)
print(map.__doc__)
print(map.__class__)
print(map.__name__)
print(type(map))

print(filter.__doc__)
print(filter.__dict__)
print(filter.__module__)
print(filter.__name__)
