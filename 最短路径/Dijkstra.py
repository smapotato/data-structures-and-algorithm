class Edge():  # 边
    def __init__(self, a, b, weight):
        self.a = a  # 第一个顶点
        self.b = b  # 第二个顶点
        self.weight = weight  # 权值

    def v(self):
        return self.a

    def w(self):
        return self.b

    def wt(self):
        return self.weight

    def other(self, x):  # 返回x顶点连接的另外一个顶点
        if x == self.a or x == self.b:
            return self.a if x == self.a else self.b

    def __lt__(self, other):  # 小于号重载
        return self.weight < other.wt()

    def __le__(self, other):  # 大于号重载'
        return self.weight > self.wt()

    def __ge__(self, other):  # 大于等于号重载
        return self.weight >= other.wt()

    def __eq__(self, other):  # 等于号重载
        return self.weight == other.wt()


class DenseGraph(object):
    """稠密图 - 邻接矩阵"""

    def __init__(self, n, directed):
        self.n = n  # 图中的点数
        self.m = 0  # 图中的边数
        self.directed = directed  # bool值，表示是否为有向图
        self.g = [[None for _ in range(n)] for _ in range(n)]  # 矩阵初始化都为False的二维矩阵

    def V(self):
        # 返回图中点数
        return self.n

    def E(self):
        # 返回图中边数
        return self.m

    def addEdge(self, v, w, weight):
        # v和w中增加一条边，v和w都是[0,n-1]区间
        if v >= 0 and v < n and w >= 0 and w < n:
            if self.hasEdge(v, w):
                return None
            self.g[v][w] = Edge(v, w, weight)
            if not self.directed:
                self.g[w][v] = Edge(w, v, weight)
            self.m += 1

    def hasEdge(self, v, w):
        # v和w之间是否有边，v和w都是[0,n-1]区间
        if v >= 0 and v < n and w >= 0 and w < n:
            return self.g[v][w] != None

    class adjIterator(object):
        """相邻节点迭代器"""

        def __init__(self, graph, v):
            self.G = graph  # 需要遍历的图
            self.v = v  # 遍历v节点相邻的边
            self.index = 0  # 遍历的索引

        def __iter__(self):
            return self

        def __next__(self):
            while self.index < self.G.V():
                # 当索引小于节点数量时遍历，否则为遍历完成，停止迭代
                if self.G.g[self.v][self.index]:
                    r = self.G.g[self.v][self.index]
                    self.index += 1
                    return r
                self.index += 1
            raise StopIteration()


class SparseGraph(object):
    """稀疏图- 邻接表"""

    def __init__(self, n, directed):
        self.n = n  # 图中的点数
        self.m = 0  # 图中的边数
        self.directed = directed  # bool值，表示是否为有向图
        self.g = [[] for _ in range(n)]  # 矩阵初始化都为空的二维矩阵

    def V(self):
        # 返回图中点数
        return self.n

    def E(self):
        # 返回图中边数
        return self.m

    def addEdge(self, v, w, weight):
        # v和w中增加一条边，v和w都是[0,n-1]区间
        if v >= 0 and v < n and w >= 0 and w < n:
            # 考虑到平行边会让时间复杂度变为最差为O(n)
            # if self.hasEdge(v, w):
            #   return None
            self.g[v].append(Edge(v, w, weight))
            if v != w and not self.directed:
                self.g[w].append(Edge(w, v, weight))
            self.m += 1

    def hasEdge(self, v, w):
        # v和w之间是否有边，v和w都是[0,n-1]区间
        # 时间复杂度最差为O(n)
        if v >= 0 and v < n and w >= 0 and w < n:
            for i in self.g[v]:
                if i.other(v) == w:
                    return True
            return False

    class adjIterator(object):
        """相邻节点迭代器"""

        def __init__(self, graph, v):
            self.G = graph  # 需要遍历的图
            self.v = v  # 遍历v节点相邻的边
            self.index = 0  # 遍历的索引

        def __iter__(self):
            return self

        def __next__(self):
            if len(self.G.g[self.v]):
                # v有相邻节点才遍历
                if self.index < len(self.G.g[self.v]):
                    r = self.G.g[self.v][self.index]
                    self.index += 1
                    return r
                else:
                    raise StopIteration()
            else:
                raise StopIteration()


class IndexMinHeap():  # 最小索引堆
    def __init__(self, n):
        self.capacity = n  # 堆的最大容量
        self.data = [0] + [-1 for _ in range(n)]  # 创建堆
        self.indexs = [0]  # 创建索引堆
        self.count = 0  # 元素数量

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

     def __contain__(self, i):
        # 最小堆中是否包含i索引的元素
        return self.data[i] != -1

    def insert(self, i, item):  # 插入元素
        self.data[i] = item
        self.indexs.append(i)
        self.count += 1
        self.shiftUp(self.count)

    def shiftUp(self, i):
        while i // 2 > 0:
            if self.data[self.indexs[i]] < self.data[self.indexs[i // 2]]:
                self.indexs[i // 2], self.indexs[i] = self.indexs[i], self.indexs[i // 2]
                i = i // 2
            else:
                break

    def extractMin(self):  # 出堆
        ret = self.data[self.indexs[1]]
        self.indexs[1] = self.indexs[self.count]
        self.count -= 1
        self.indexs.pop()
        self.shiftDown(1)
        return ret

    def extractMinIndex(self):  # 出堆返回索引
        ret = self.indexs[1]
        self.indexs[1] = self.indexs[self.count]
        self.count -= 1
        self.indexs.pop()
        self.shiftDown(1)
        return ret

    def shiftDown(self, i):  # 将堆的索引位置元素向下移动到合适位置，保持最小堆
        while 2 * i <= self.count:
            j = 2 * i
            if j + 1 <= self.count and self.data[self.indexs[j + 1]] < self.data[self.indexs[j]]:  # 最小子节点
                j += 1
            if self.data[self.indexs[j]] < self.data[self.indexs[i]]:
                self.indexs[j], self.indexs[i] = self.indexs[i], self.indexs[j]
                i = j
            else:
                break

    def getItem(self, i):  # 根据索引获取数值
        if i > 0 and i <= self.count:
            return self.data[i]
        else:
            return None

    def change(self, i, item):  # 改变i索引位置的数值
        if i >= 0:
            self.data[i] = item
            j = self.indexs.index(i)
            self.shiftUp(j)
            self.shiftDown(j)


class Dijkstra():  # Dijkstra算法(不能有负权边)求从s点到所有节点最短路径，从原点s开始遍历相邻节点，选取权值最小的边连接的顶点，依次遍历选取最小边并做松弛操作
    def __init__(self, graph, s):
        self.G = graph  # 图
        self.ipq = IndexMinHeap(self.G.V())  # 最小索引堆，存权值
        self.s = s  # 原点，表示从此节点到所有节点求最短路径
        self.marked = [False for _ in range(self.G.V())]  # 用于标记已经找到到节点的最短路径，初始都为False
        self.distTo = [0 for _ in range(self.G.V())]  # 从原点到每个节点的权值，初始都为0
        self.fromed = [None for _ in range(self.G.V())]  # 记录此节点来自哪个节点的连接，存储边。None表示未被访问过

        # Dijkstra
        self.marked[s] = True
        self.ipq.insert(s, self.distTo[s])
        while not self.ipq.isEmpty():
            v = self.ipq.extractMinIndex()
            self.marked[v] = True  # distTo[v]就是s到v的最短距离，v确认找到最短路径
            # 松弛操作
            adj = self.G.adjIterator(self.G, v)
            for e in adj:
                w = e.other(v)
                # 如果w还没有确定找到最短路径
                if not self.marked[w]:
                    # 如果w还未被访问过，或经过v的最短路径再到w节点的权值小于w之前被访问时记录的路径，则用经过v再到w的路径替代
                    if not self.fromed[w] or self.distTo[w] + e.wt() < self.distTo[w]:
                        self.distTo[w] = self.distTo[v] + e.wt()
                        self.fromed[w] = e
                        if w in self.ipq:
                            self.ipq.change(w, self.distTo[w])
                        else:
                            self.ipq.insert(w, self.distTo[w])

    def shortestPathTo(self, w):
        # 从原点到w节点的权值
        return self.distTo[w]

    def hasPathTo(self, w):
        # 从原点到w是否有路径
        return self.marked[w]

    def shortestPath(self, w):  # 从原点到w的最短路径
        s = []
        e = self.fromed[w]
        while e:
            s.append(e)
            e = self.fromed[e.v()]
        s.reverse()
        return s

    def showPath(self, w):  # 输出路径
        s = self.shortestPath(w)
        i = 0
        while i < len(s):
            print(s[i].v())
            if i == len(s) - 1:
                print(s[i].w())
            i += 1
