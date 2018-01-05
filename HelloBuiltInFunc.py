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


print("=====1.abs(*args, **kwargs)======")
#1.abs(*args, **kwargs):返回x的绝对值，，如果x为str、one，list，tuple，dict,则会报错，True/False的绝对值返回1，0
a,b = 12.0,-1
print(abs(a))
print(abs(b))
print(abs(True))#1
print(abs(False))#0
# print(abs((1,2,))) TypeError
#print(abs([1,-1])) TypeError: bad operand type for abs():'list'
#print(abs('-1')) TypeError
#print(abs({'a':-1,})) TypeError

print("=====2.all(*args, **kwargs)======")
#2.all(*args, **kwargs):Return True if bool(x) is True for all values x in the iterable.
    #If the iterable is empty, return True.
print(all([1,2,3])) #True
print(all([-1,2,3]))#True
print(all([]))#True
print(all('a')) #True

print("=====3.bool()======")
#3.bool():
#Return a Boolean value, i.e. one of True or False. x is converted using the standard truth testing procedure. If x is false or omitted, this returns False; otherwise it returns True. The bool class is a subclass of int (see Numeric Types — int, float, complex). It cannot be subclassed further.
#Its only instances are False and True (see Boolean Values).
print(bool())#False

print(bool(True)) #True
print(bool(False)) #False

print(bool(1)) #True
print(bool(0)) #False
print(bool(-1)) #True

print(bool('123')) #True
print(bool('')) #False:空字符串返回False

print(bool([])) #False:空list
print(bool([1,2])) #True

print(bool(())) #False:空tuple
print(bool((1,))) #True

print(bool({})) #False:空dict
print(bool({'a':1,}))#True

#4.any(*args, **kwargs)：
# Return True if bool(x) is True for any x in the iterable.
# If the iterable is empty,return False.
print("=====4.any()======")
print(any((1,2,3,0))) #True
print(any((0,)))#False
print(any(()))#empty:False
print(any({'a',0}))#True
print(any([0,0]))#False
print(any(('','')))#False
print(any('')) #False
print(any((False,)))#False

#5.ascii(*args, **kwargs):
#Return an ASCII-only representation of an object.
#As repr(), return a string containing a printable representation of an
#object, but escape the non-ASCII characters in the string returned by
#repr() using \\x, \\u or \\U escapes. This generates a string similar
#to that returned by repr() in Python 2.
print("=====5.ascii()======")
print(ascii("zc"))#zc
print(repr("zc"))#zc
print(ascii(1))#1
print(ascii(0))#0
print(ascii(1100))#1100
print(ascii((1,2)))#(1,2)

#6.bin(*args, **kwargs):

#Return the binary representation of an integer.
#     >>> bin(2796202)
#      '0b1010101010101010101010'
print("=====6.bin()======")
print(bin(0))#0b0
print(bin(1))
print(bin(1100))
