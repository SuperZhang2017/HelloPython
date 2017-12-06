#bulit_in function 内建函数
#1.cmp()--比较(python2) operater(python3)
a,b = 1,-1
import operator
#判断是否小于，返回布尔值
print(operator.lt(a,b))
#判断是否大于，返回布尔值
print(operator.gt(a,b))
#判断是否等于，返回布尔值
print(operator.eq(a,b))
#
#2.type()--得到一个对象的类型，并返回相应的type对象
print(type(4))
print(type('string'))
print(type([1,2,3]))
print(type((1,)))
print(type((1)))
print(type({'c':1,'d':2}))
print(type(None))
print(type(type(4)))
#3.str()--返回对象适合可读性好的字符串表示
# repr()--返回一个对象的字符串
m=[1,2,3]
print(str(m))
print(m)
print(operator.eq(m,str(m)))
print(repr(m)==str(m))

n= eval(repr(m))
print(n==m)

l=eval(str(m))
print(l==m)

class Foo:
    pass
foo=Foo()
class Bar(object):
    pass
bar=Bar()

print(type(Foo))
print(type(foo))
print(type(Bar))
print(type(bar))
print(type(''))
#python3：int long统一 ，python2：long型1l表示
print(type(100000))
print(isinstance(bar,object))
#demo
#types()
#id()
x = 'hello python'
print(id(x))
x = 'hello Python'
print(id(x))
x= 'hello Python'
print(id(x))

def test(c):
    print("test before ")
    print(id(c))
    c+=2
    print("test after ")
    print(id(c))
    return c

if __name__=="__main__":
    a=2
    print("main before invoke test")
    print(id(a))
    n=test(a)
    print("main afterf invoke test")
    print(a)
    print(id(a))

#Python参数传递采用的肯定是“传对象引用”的方式。这种方式相当于传值和传引用的一种综合。
#如果函数收到的是一个可变对象（比如字典或者列表）的引用，就能修改对象的原始值－－相当于通过“传引用”来传递对象。
#如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，就不能直接修改原始对象－－相当于通过“传值'来传递对象。