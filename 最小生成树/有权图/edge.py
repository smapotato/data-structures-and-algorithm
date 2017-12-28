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
