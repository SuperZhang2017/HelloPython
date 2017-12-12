#迭代器
#1.迭代序列
myTuple =(1,2,33,)
i= iter(myTuple)
for m in i:
    print(m)
#2.字典迭代
di={'a':1,'b':2}
for eachVar in di:
    print(eachVar,di[eachVar])
    print(eachVar,di.get(eachVar))

#等价于
for eachVar in di.keys():
    print(eachVar,di.get(eachVar))

for i,eachVar in enumerate(di):
    print(i,eachVar)

for item  in  di.items():
    print(item)

for key in di.keys():
    print(key,di[key])
#3.文件迭代
myFile = open("../../a.txt")
for eachLine in myFile:
    print(eachLine)