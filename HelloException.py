#异常exception
# 一、常见异常
#1.NameError
#fo0
#2.ZeroDivisionError
#1/0
#3.SyntaxError语法错误，常见
#for
# 4.IndexError
# aList = []
# aList[0]
# 5.KeyError
# aDict = {'a':1, 'b':2}
# print(aDict['ab'])
# 6.FileNotFoundError
# f = open("a.txt")
# 二、异常处理
# 1.try..except
# 2.try..finally
try:
    f = open("a.txt")
except IOError as e:
    print(e)

def safe_float(obj):
    try:
        reval = float(obj)
    except ValueError:
        reval = 'could not convert to float'
    except TypeError:
        reval ='obj type could not convert to float'

    return reval

print(safe_float('abc'))
print(safe_float(123))
print(safe_float(5453.3400))


def safe_float1(obj):
    try:
        re = float(obj)
    except (ValueError,TypeError):
        re = 'argument must a number or numeric string'
    return re

print(safe_float1('abc'))



def a(obj):
    try:
        re = float(obj)
    except Exception as e:
        print(e)

print(a('BC'))