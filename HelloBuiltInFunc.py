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

print("=====7.callable()======")
#7.callable(i_e_, some_kind_of_function)
"""
 Return whether the object is callable (i.e., some kind of function).

 Note that classes are callable, as are instances of classes with a
 __call__() method.
 """
print(callable(0))#False
print(callable(map)) #True
print(callable(filter))#True

from HelloBubbleSort import BubbleSort
print(callable(BubbleSort))#True:classes are callable

def te():
    pass
print(callable(te))#True

print("=====8.chr()======")
#8.chr(*args, **kwargs): # real signature unknown
""" Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff. """

print(chr(49))#'1'
print(type(chr(49)))
print(chr(65))#'A'
print(chr(90))#'Z'
print("=====9.copyright()======")
#9.copyright(*args, **kwargs): # real signature unknown
"""
    interactive prompt objects for printing the license text, a list of
        contributors and the copyright notice.
"""
print(copyright())
print("=====10.compile()======")
#10.compile(source, filename, mode[, flags[, dont_inherit]])
"""
  Compile source into a code object that can be executed by exec() or eval().

  The source code may represent a Python module, statement or expression.
  The filename will be used for run-time error messages.
  The mode must be 'exec' to compile a module, 'single' to compile a
  single (interactive) statement, or 'eval' to compile an expression.
  The flags argument, if present, controls which future statements influence
  the compilation of the code.
  The dont_inherit argument, if true, stops the compilation inheriting
  the effects of any future statements in effect in the code calling
  compile; if absent or false these statements do influence the compilation,
  in addition to any features explicitly specified.
"""
"""
source -- 字符串或者AST（Abstract Syntax Trees）对象。。
filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
flags和dont_inherit是用来控制编译源码时的标志
"""
str = "for i in range(10):print(i)"
c = compile(str,'','exec')
print(exec(c))

str = "3*4+5"
d = compile(str,'','eval')
print(eval(d))

#11.delattr(x, y):  # real signature unknown; restored from __doc__
"""
Deletes the named attribute from the given object.

delattr(x, 'y') is equivalent to ``del x.y''
"""
#12.divmod(x, y): # known case of builtins.divmod--返回整除部分和余数的元组
""" Return the tuple (x//y, x%y).  Invariant: div*y + mod == x. """
x ,y = 10, 11
z = divmod(10,11)
print(z)

#13.eval(*args, **kwargs):  # real signature unknown
"""
Evaluate the given source in the context of globals and locals.

The source may be a string representing a Python expression
or a code object as returned by compile().
The globals must be a dictionary and locals can be any mapping,
defaulting to the current globals and locals.
If only globals is given, locals defaults to it.
"""
#eval(source,globals,locals)
print(eval("{'a':1,'b':2}"),{'a':2,'b':1})
# 可以把list,tuple,dict和string相互转化。
aList = eval('[1,2,3]')#str-->List
print(aList)
aTuple = eval('(1,2,)')
print(aTuple)
aDict = eval('{"c":1,"d":2}')
print(aDict)
print(eval('aList')) #List -->str
print(type('aList'))


