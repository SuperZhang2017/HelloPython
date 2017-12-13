#冒泡算法
class BubbleSort(object):
    def __init__(self,datas):
        self.datas = datas
        self.l= len(datas)

    def bubbleSort(self):
       for i in range(self.l-1):
           for j in range(self.l-i-1):
               if(seq[j+1]<seq[j]):
                   seq[j],seq[j+1] = seq[j+1],seq[j]
       return seq


if __name__=="__main__":
    data = input("please enter number:")
    seq = data.split()
    datas = [int(seq[i]) for i in range(len(seq))]

    o = BubbleSort(datas)
    print(type(o))
    result = o.bubbleSort()

    print(result)