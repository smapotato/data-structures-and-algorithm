class BinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0
    def insert(self,k):
        self.heaplist.append(k)#要考虑堆的容量
        self.currentsize += 1
        self.shiftup(self.currentsize)
    def shiftup(self,i):
        while i//2 >0:
            if self.heaplist[i] > self.heaplist[i//2]:
                self.heaplist[i],self.heaplist[i//2] = self.heaplist[i//2],self.heaplist[i]
            i = i//2
    def delmin(self):
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.currentsize -= 1
        self.heaplist.pop()
        self.shiftdown(1)
    def shiftdown(self,i):
        while 2*i <= self.currentsize:
            j = 2*i
            if j+1<=self.currentsize and self.heaplist[j+1]>self.heaplist[j]:#求最大子节点
                j += 1
            if self.heaplist[i] < self.heaplist[j]:
                self.heaplist[i],self.heaplist[j] = self.heaplist[j],self.heaplist[i]
                i = j
            else:
                break
    def buildheap(self,alist):
        i = len(alist)//2
        self.currentsize = len(alist)
        self.heaplist = [0] + alist[:]
        while i > 0:
            self.shiftdown(i)
            i -= 1
    def isEmpty(self):
        return self.currentsize == 0
