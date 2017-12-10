#条件和循环
#I.条件
#1.if
#2.else
#3.elif
li=[1,2,3]
if 1 not in li:
    print("not in ")
else:
    print("in")

if 1 in li:
    print("1 in")
elif 4 not in li:
    print("4 not in")
else:
    print("good")

#4 条件表达式 三元表达式
# x if C else y
x, y = 3, 4
smaller = x if x<y else y
print(smaller)

#5.while 语句
count = 0
while(count<9):
    print('the index is:',count)
    count+=1

#6.for
# for a in iterable:
     #
liA=['A','B','C']
#方法一：序列项迭代
for eachName in liA:
    print(eachName)
s = 'Names'
for v in s:
    print('current letter:',v)
#方法二：序列索引迭代
for i in range(len(liA)):
    print(liA[i])

#方法三：使用enumerate函数，项和索引迭代
for i,eachLi in enumerate(liA):
    print(i+1,eachLi)

    
