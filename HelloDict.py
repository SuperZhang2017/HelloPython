#字典dict--映射类型
#1.创建字典和赋值
di= dict(([1,2],['a','b']))
print(di)
dic = {}.fromkeys(('a','b'),(-1,2))
print(dic)
dic1 = {}.fromkeys(('a','b'),1)
print(dic1)
dic2 = {}.fromkeys(('a','b'))
print(dic2)
#2.访问字典中的值
print(di[1])#根据key取value
#3.遍历
#3.1第一种方法
for key in di.keys():
    print(key,di[key])
    print('key=%s,value=%s'%(key,di[key]))
#3.2第二种方法
for key in di:
    print('key=%s,value=%s'%(key,di[key]))

print('a' in dic2)#判断key 在字典中
print(1 in dic1)#不能以此判断value在dic中

print(di.keys())#获取所有key列表
print(di.values())#获取所有value列表
print(di.items())#获取所有key:value条目
print(type(di.items()))
for key,value in di.items():
    print(key,value)
#4.更新字典
di[1]='aa'
print(di)
didi =di.update()
print(didi)

print(di.get(1))#有返回value值，没有key则返回默认值None
print(di.get(2,'a'))
print(di[1])#有返回value值，没有key则返回keyerror错误
#5.删除字典元素和字典
del di[1]
print(di)
di.clear()#清空字典条目
print(di)
#del di
#print(di)#error,已经删除字典di对象
print(id(di))
#6.比较两个dict
d1={'a':1,'b':2}
d2={'a':2,'b':3}
import operator
re = operator.eq(d1,d2)
print(re)
print(len(d1)>len(d2))

