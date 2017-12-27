from random import randint


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

    def addEdge(self, v, w):
        # v和w中增加一条边，v和w都是[0,n-1]区间
        if v >= 0 and v < n and w >= 0 and w < n:
            # 考虑到平行边会让时间复杂度变为最差为O(n)
            # if self.hasEdge(v, w):
            #   return None
            self.g[v].append(w)
            if v != w and not self.directed:
                self.g[w].append(v)
            self.m += 1

    def hasEdge(self, v, w):
        # v和w之间是否有边，v和w都是[0,n-1]区间
        # 时间复杂度最差为O(n)
        if v >= 0 and v < n and w >= 0 and w < n:
            # for i in self.g[v]:
            #   if i == w:
            #       return True
            # return False
            if w in self.g[v]:
                return True
            else:
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


class Component():  # 深度优先遍历和连通分量
    def __init__(self, graph):
        self.G = graph  # 图
        self.count = 0  # 联通分量
        self.visited = [False for _ in range(self.G.V())]  # 记录每个节点是否被遍历
        self.id = [-1 for _ in range(self.G.V())]  # 相连节点的id相同,初始都为-1
        i = 0
        while i < self.G.V():
            if not self.visited[i]:
                self.dfs(i)
                self.count += 1
            i += 1

    def dfs(self, v):  # 深度优先遍历
        self.visited[v] = True
        # print(v)  深度优先的顺序
        self.id[v] = self.count
        adj = self.G.adjIterator(self.G, v)  # 找到v节点所有相邻的点，进行迭代遍历
        for i in adj:
            if not self.visited[i]:
                self.dfs(i)

    def isConnected(self, v, w):  # 判断节点是否相连
        if v >= 0 and v < self.G.V() and w >= 0 and w < self.G.V():
            return self.id[v] == self.id[w]


if __name__ == "__main__":
    n = 13
    g1 = SparseGraph(13, False)
    for _ in range(50):
        a = randint(0, n - 1)
        b = randint(0, n - 1)
        g1.addEdge(a, b)
    for v in range(13):
        adj = SparseGraph.adjIterator(g1, v)
        # print("{}{}".format(v,list(adj)))
    component1 = Component(g1)
    print(component1.count)
