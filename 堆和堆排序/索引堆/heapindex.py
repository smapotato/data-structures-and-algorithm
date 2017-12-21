cclass IndexMaxHeap:
    def __init__(self,n):
        self.capacity = n #堆容量
        self.heaplist = [0 for _ in range(n)] #创建堆
        self.currentsize = 0
        self.indexes = [0]#创建索引堆

    def insert(self, k, item):
        self.heaplist[k] = item
        self.indexes.append(k)
        self.currentsize += 1
        self.shiftup(self.currentsize)

    def shiftup(self, i):  # 索引堆中, 数据之间的比较根据heaplist的大小进行比较, 但实际操作的是索引
        while i > 1 and self.heaplist[self.indexes[i//2]] < self.heaplist[self.indexes[i]]:
            self.indexes[i//2], self.indexes[i] = self.indexes[i], self.indexes[i//2]
            i = i//2

    def extractMax(self):  # 从最大索引堆中取出堆顶元素, 即索引堆中所存储的最大数据
        ret = self.heaplist[self.indexes[1]]
        self.indexes[1], self.indexes[self.currentsize] = self.indexes[self.currentsize], self.indexes[1]
        self.currentsize -= 1
        self.shiftdown(1)
        return ret

    def shiftdown(self, i):
        while 2 * i <= self.currentsize:
            j = 2 * i
            if j + 1 <= self.currentsize and self.heaplist[self.indexes[j + 1]] > self.heaplist[self.indexes[j]]:
                j += 1
            if self.heaplist[self.indexes[j]] >= self.heaplist[self.indexes[i]]:
                self.indexes[i], self.indexes[j] = self.indexes[j], self.indexes[i]
                i = j
            else:
                break

    def extractMaxIndex(self):  # 从最大索引堆中取出堆顶元素的索引
        ret = self.indexes[1] - 1
        self.indexes[1], self.indexes[self.currentsize] = self.indexes[self.currentsize], self.indexes[1]
        self.currentsize -= 1
        self.shiftdown(1)
        return ret

    def getitem(self, i):
        return self.heaplist[i + 1]

    def change(self, i, newitem):  # 将最大索引堆中索引为i的元素修改为newItem
        if i not in self.heaplist:
            return "not exist"
        self.heaplist[i] = newitem
        """
        for j in range(1, self.currentsize + 1):
            if self.indexes[j] == i:
                self.shiftup(j)
                self.shiftdown(j)
        """
        i=self.indexes.index(k)  
        self.shiftDown(i)
        self.shiftUp(i)


