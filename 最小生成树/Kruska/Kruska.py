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


class UnionFind():  # 路径压缩Path Compression，Quick Union，每个元素的组指向（等于）父节点的元素，根节点指向（等于）自身
    def __init__(self, n):
        self.count = n
        self.parent = list(range(n))
        self.rank = [1 for _ in range(n)]  # rank[i]表示以i为根的集合表示的树的层数

    def find(self, p):  # 查找元素对应的组
        if p >= 0 and p <= self.count:  # 路径压缩，自身指向由父节点变为根节点
            if p != self.parent[p]:
                self.parent[p] = self.find(self.parent[p])
            return self.parent[p]

    def isConnected(self, p, q):  # p q两个元素是否连接，返回两个元素的组是否相等
        return self.find(p) == self.find(q)

    def unionElements(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:  # pq根节点的组相等，不需要并，直接返回
            return None
        if self.rank[pRoot] < self.rank[qRoot]:
            # 不需要维护rank，因为rank[i]表示i为根的节点的树的层数。
            # pRoot指向qRoot后，qRoot的层数不变，pRoot的根节点变成qRoot，再find时则不会再找到pRoot
            self.parent[pRoot] = qRoot
        elif self.rank[pRoot] > self.rank[qRoot]:
            self.parent[qRoot] = pRoot
        else:
            self[pRoot] = qRoot
            self.rank[qRoot] += 1


"""切分定理：给定任意切分，横切边中权值最小的边必然属于最小生成树"""


class KruskaMST():  # Kruskal最小生成树，先将边根据权值排序，然后依次取最小的边，只要不形成环
    def __init__(self, graph):
        self.G = graph  # 传入图
        self.pq = MinHeap()  # 最小索引堆，存权值
        self.uf = UnionFind(self.G.V())
        self.mst = []  # 记录被选取的边
        self.mstWeight = 0  # 记录最小生成树的总权值
        for i in range(self.G.V()):  # 遍历每个节点
            adj = self.G.adjIterator(self.G, i)
            for e in adj:  # 遍历与节点相连的所有边
                if e.v() < e.w():  # 因直接遍历会导致每条边被遍历两次，所以做判断，使每条边被插入到堆中一次
                    self.pq.insert(e)
        while not self.pq.isEmpty() and len(self.mst) < self.G.V() - 1:
            e = self.pq.delMin()
            # 判断此边是否会导致成环
            if self.uf.isConnected(e.v(), e.w()):
                continue
            self.mst.append(e)
            self.uf.unionElements(e.v(), e.w())
        self.mstWeight = sum([i.wt() for i in self.mst])

    def mstEdges(self):
        # 查询最小生成树的边
        return self.mst

    def result(self):
        # 返回最小生成树的权值
        return self.mstWeight

