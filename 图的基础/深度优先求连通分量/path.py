class Path():  # 寻找路径
    def __init__(self, graph, s):
        self.G = graph  # 图
        self.s = s  # 从s节点开始寻找其他节点的路径
        self.visited = [False for _ in range(self.G.V())]  # 记录每个节点是否被遍历
        self.fromed = [-1 for _ in range(self.G.V())]  # 记录此节点来自那个节点的连接
        self.dfs(s)  # 寻找路径

    def dfs(self, v):  # 深度优先遍历
        self.visited[v] = True
        # print(v)  深度优先的顺序
        adj = self.G.adjIterator(self.G, v)  # 找到v节点所有相邻的点，进行迭代遍历
        for i in adj:
            if not self.visited[i]:
                self.fromed[i] = v  # 对还未遍历的节点,先将此节点的from修改为v，表示i节点来自v节点相连
                self.dfs(i)

    def hasPath(self, w):  # w与v是否有路径
        if w >= 0 and w < self.G.V():
            return self.visited[w]

    def path(self, w):  # 从v到w的路径
        s = []
        p = w
        while p != -1:
            s.append(p)
            p = self.fromed[p]
        s.reverse()
        return s

    def showPath(self, w):  # 展示路径
        s = self.path(w)
        for i in s:
            print(i)
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
    # print(component1.count)
    path1 = Path(g1, 0)
    print(path1.path(8))
    path1.showPath(8)
