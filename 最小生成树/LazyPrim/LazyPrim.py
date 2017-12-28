class Edge():  # 边
    def __init__(self, a, b, weight):
        self.a = a  # 第一个顶点
        self.b = b  # 第二个顶点
        self.weight = weight  # 权值

    def v(self):
        return self.a

    def w(self):
        return b

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


class MinHeap():  # 最小堆
    def __init__(self):
        self.data = [0]  # 创建堆
        self.count = 0  # 元素数量

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def insert(self, item):  # 插入元素
        self.data.append(item)
        self.count += 1
        self.shiftUp(self.count)

    def shiftUp(self, i):
        while i // 2 > 0:
            if self.data[i] < self.data[i // 2]:
                self.data[i // 2], self.data[i] = self.data[i], self.data[i // 2]
                i = i // 2
            else:
                break

    def delMin(self):  # 删除最小元素
        ret = self.data[1]
        self.data[1] = self.data[self.count]
        self.count -= 1
        self.data.pop()
        self.shiftDown(1)
        return ret

    def shiftDown(self, i):
        while 2 * i <= self.count:
            j = 2 * i
            if j + 1 <= self.count and self.data[j + 1] < self.data[j]:  # 最小子节点
                j += 1
            if self.data[j] < self.data[i]:
                self.data[j], self.data[i] = self.data[i], self.data[j]
                i = j
            else:
                break

"""切分定理：给定任意切分，横切边中权值最小的边必然属于最小生成树"""
class LazyPrimMST():  # 最小生成树T，每次选取横切边中权值最小的边，将另一端顶点加入树中
    def __init__(self, graph):
        self.G = graph  # 传入图
        self.pq = MinHeap()  # 最小堆，用于选择权值最小的边
        self.marked = [False for _ in range(self.G.V())]  # 用于标记已经被选取为树的节点，初始为False
        self.mst = []  # 记录被选取的边
        self.mstWeight = 0  # 记录最小生成树的总权值
        self.visit(0)
        while not self.pq.isEmpty():  # 取出权值最小的边
            e = self.pq.delMin()
            if self.marked[e.v()] == self.marked[e.w()]:  # 如果e不是横切边（比如两个顶点都已经加入树中）
                continue
            # 选取e这条边，组成最小生成树
            self.mst.append(e)
            # 此时e边两个顶点必有一个未加入树中
            if not self.marked[e.v()]:
                self.visit(e.v())
            else:
                self.visit(e.w())
        self.mstWeight = sum(i.wt() for i in self.mst)

    def visit(self, v):  # 访问
        if not self.marked[v]:  # self.marked[v]为False，表示该节点还未被加入树中
            self.marked[v] = True
            adj = self.G.adjIterator(self.G, v)
            for i in adj:
                if not self.marked[i.other(v)]:  # 与v相连接的另一端还未被加入树中，则这一条边为横切边，加入到最小堆中
                    self.pq.insert(i)  # 此处Edge类重载运算符，可直接放入堆中进行计算

