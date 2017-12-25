#函数
#1.定义、调用
def test(a,b):
    return a * b
print(test(b=1,a=2))
print(test(1,2))
print(type(test))
#2.参数组：无显示定义参数的函数
#func(position_args,keyword_args,*tuple_args,**dict_args)
#tuple_args:元组形式体现的非关键字参数组
#dict_args：装有关键字参数的字典

def te(*a1,**a2):
    return a1

print(te((1,2,3)))#((1,2,3),)
print(te(*(1,2,3)))#(1,2,3)
print(te(1))#(1,)

def tt(**a):
    return a
print(tt(**{'a':1,'b':2}))
print(tt(a=1,b=3))#{'a':1,'b':3}
print(tt(a=1,b=3,c=4).get('a'))
