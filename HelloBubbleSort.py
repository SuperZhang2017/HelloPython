#冒泡算法
class BubbleSort(object):
    def __init__(self,datas):
        self.datas = datas
        self.l= len(datas)

    def bubbleSort(self):
       for i in range(self.l-1):
           for j in range(self.l-i-1):
               if(self.datas[j+1]<self.datas[j]):
                   self.datas[j],self.datas[j+1] = self.datas[j+1],self.datas[j]
       return self.datas


if __name__=="__main__":
    datas = input("please enter number:")
    datas = datas.split()
    datas = [int(datas[i]) for i in range(len(datas))]

    o = BubbleSort(datas)
    print(type(o))
    result = o.bubbleSort()

    print(result)